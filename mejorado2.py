from fbchat_muqit import Client
import asyncio


async def bot():
    client = Client(cookies_file_path="prueba2.json")

    await client.start()

    grupo = input("Escribe el ID del grupo: ").strip()
    apodo_correcto = input("Escribe el apodo para todos: ")

    asyncio.create_task(client.start_listening())

    print("\n🤖 Bot conectado")
    print("👀 Vigilando los apodos de todos los miembros...\n")

    while True:
        try:
            thread = (await client.fetch_thread_info([grupo]))[0]

            miembros = thread.all_participants
            apodos = thread.participants_nickname or {}

            for miembro in miembros:
                usuario = str(miembro.id)

                apodo_actual = apodos.get(usuario)

                print(
                    f"Usuario: {usuario} | "
                    f"Apodo: {apodo_actual}"
                )

                if apodo_actual != apodo_correcto:
                    print("❌ Apodo diferente")
                    print("🔧 Restaurando...")

                    await client.change_nickname(
                        grupo,
                        usuario,
                        apodo_correcto
                    )

                    print(
                        f"✅ {usuario} → {apodo_correcto}"
                    )

                    await asyncio.sleep(2)

            await asyncio.sleep(8)

        except Exception as e:
            print(f"❌ Error: {e}")
            await asyncio.sleep(10)


asyncio.run(bot())
