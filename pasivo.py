from fbchat_muqit import Client
import asyncio


async def bot():
    client = Client(cookies_file_path="prueba2.json")

    await client.start()

    grupo = input("Escribe el ID del grupo: ").strip()
    apodo_correcto = input("Escribe el apodo para todos: ")

    print("\n🤖 Bot conectado")
    print("👀 Vigilando los apodos de todos los miembros...\n")

    while True:
        try:
            thread = (await client.fetch_thread_info([grupo]))[0]

            miembros = thread.all_participants
            apodos = thread.participants_nickname or {}

            cambios = 0

            for miembro in miembros:
                usuario = str(miembro.id)
                apodo_actual = apodos.get(usuario)

                print(f"Usuario: {usuario} | Apodo: {apodo_actual}")

                if apodo_actual != apodo_correcto:
                    print("❌ Apodo diferente")
                    print("🔧 Cambiando...")

                    await client.change_nickname(
                        grupo,
                        usuario,
                        apodo_correcto
                    )

                    print(f"✅ Solicitud enviada: {usuario}")

                    cambios += 1

                    # Pausa entre cambios
                    await asyncio.sleep(5)

            print(f"\n📊 Cambios realizados en esta vuelta: {cambios}")
            print("⏳ Esperando 15 segundos...\n")

            await asyncio.sleep(15)

        except Exception as e:
            error = str(e)

            print(f"❌ Error: {error}")

            if "1675004" in error or "Rate limit exceeded" in error:
                print("🚨 Facebook aplicó rate limit.")
                print("⏳ Esperando 2 minutos...\n")
                await asyncio.sleep(120)
            else:
                await asyncio.sleep(30)


asyncio.run(bot())
