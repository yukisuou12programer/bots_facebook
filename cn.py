from fbchat_muqit import Client
import asyncio


async def bot_hecho():
    print("🤖 YUKI CAMBIADOR DE NOMBRES DEL GRUPO")

    client = Client(cookies_file_path="prueba2.json")

    await client.start()

    grupo = input("Escribe la ID del grupo: ").strip()
    nuevo_nombre = input("Escribe el nuevo nombre: ").strip()

    asyncio.create_task(client.start_listening())

    print("\n✅ Bot conectado")
    print(f"👥 Grupo: {grupo}")
    print(f"📝 Nombre correcto: {nuevo_nombre}")
    print("👀 Vigilando el nombre del grupo...\n")

    while True:
        try:
            # Obtener información actual del grupo
            informacion = await client.fetch_thread_info([grupo])

            if not informacion:
                print("❌ No se pudo obtener información del grupo.")
                await asyncio.sleep(10)
                continue

            grupo_info = informacion[0]
            nombre_actual = grupo_info.name

            print(f"📌 Nombre actual: {nombre_actual}")

            # Solo cambiar si realmente es diferente
            if nombre_actual != nuevo_nombre:
                print("⚠️ El nombre fue cambiado.")
                print(f"🔄 Restaurando a: {nuevo_nombre}")

                await client.change_thread_name(grupo, nuevo_nombre)

                print("✅ Nombre restaurado correctamente.")
            else:
                print("✔️ El nombre ya es correcto.")

            # Esperar antes de volver a comprobar
            await asyncio.sleep(6)

        except Exception as e:
            error = str(e)

            print(f"❌ Ocurrió un error: {error}")

            if "Message queue full" in error:
                print("⏳ La cola está llena.")
                print("🛑 Esperando 40 segundos...")
                await asyncio.sleep(40)

            elif "not currently connected" in error.lower():
                print("🔌 El cliente no está conectado.")
                print("⏳ Esperando 15 segundos...")
                await asyncio.sleep(15)

            else:
                print("⏳ Esperando 10 segundos antes de intentar nuevamente...")
                await asyncio.sleep(10)


asyncio.run(bot_hecho())
