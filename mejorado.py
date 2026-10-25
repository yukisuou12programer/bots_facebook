from fbchat_muqit import Client
import asyncio


async def bot():
    client = Client(cookies_file_path="prueba2.json")

    await client.start()

    grupo = input("Escribe la ID del grupo: ").strip()
    apodo = input("Escribe el apodo a poner: ").strip()

    asyncio.create_task(client.start_listening())

    await asyncio.sleep(2)

    try:
        threads = await client.fetch_thread_info([grupo])

        if not threads:
            print("❌ No se encontró el grupo")
            return

        thread = threads[0]

        print(f"\n📌 Nombre del grupo: {thread.name}")
        print(f"👥 Participantes: {len(thread.all_participants)}")
        print("\n🔄 Bot ejecutándose...\n")

    except Exception as e:
        print("❌ Error al obtener el grupo:", e)
        return

    while True:

        # Obtener nuevamente los participantes
        try:
            threads = await client.fetch_thread_info([grupo])

            if not threads:
                print("❌ No se encontró el grupo")
                await asyncio.sleep(30)
                continue

            thread = threads[0]

        except Exception as e:
            print("❌ Error obteniendo participantes:", e)
            await asyncio.sleep(30)
            continue

        # Cambiar apodos
        for participante in thread.all_participants:

            try:
                usuario_id = participante.id

                await client.change_nickname(
                    grupo,
                    usuario_id,
                    apodo
                )

                print(
                    f"✅ {participante.name} → {apodo}"
                )

                # Esperar entre cada cambio
                await asyncio.sleep(1)

            except Exception as e:

                error = str(e)

                if "Message queue full" in error:
                    print("⚠️ Cola llena. Esperando 40 segundos...")
                    await asyncio.sleep(40)

                elif "not currently connected" in error:
                    print("⚠️ Cliente desconectado. Esperando 30 segundos...")
                    await asyncio.sleep(30)

                else:
                    print(
                        f"❌ Error con {participante.name}: {e}"
                    )
                    await asyncio.sleep(5)

        # Esperar antes de volver a recorrer todo
        print("\n⏳ Esperando 30 segundos para repetir...\n")
        await asyncio.sleep(30)


asyncio.run(bot())
