from fbchat_muqit import Client
import asyncio

client = None
grupo = None
apodo = None


async def on_nickname_change(event_data, message):
    try:
        print("📢 EVENTO DE APODO RECIBIDO")

        if str(message.thread_id) != str(grupo):
            return

        usuario_id = str(event_data.participant_id)
        nuevo_apodo = event_data.nickname

        print(f"👤 Usuario: {usuario_id}")
        print(f"📝 Nuevo apodo: {nuevo_apodo}")

        if nuevo_apodo == apodo:
            print("✔ Ya tiene el apodo correcto")
            return

        print(f"🔧 Restaurando → {apodo}")

        await client.change_nickname(
            grupo,
            usuario_id,
            apodo
        )

        print(f"✅ Apodo restaurado para {usuario_id}")

    except Exception as e:
        print(f"❌ Error en evento de apodo: {e}")


async def bot():
    global client
    global grupo
    global apodo

    client = Client(
        cookies_file_path="prueba2.json"
    )

    await client.start()

    grupo = input(
        "escribe la id del grupo: "
    ).strip()

    apodo = input(
        "escribe apodo a poner: "
    ).strip()

    # Registrar el evento
    client.event(on_nickname_change)

    # Iniciar escucha
    await asyncio.create_task(client.start_listening())

    await asyncio.sleep(2)

    # Obtener grupo
    threads = await client.fetch_thread_info([grupo])

    if not threads:
        print("no se encontro grupo")
        return

    thread = threads[0]

    print(f"Nombre del grupo {thread.name}")
    print(
        "participantes encontrados:",
        len(thread.all_participants)
    )

    print("informacion del grupo:\n")

    # Cambiar apodos inicialmente
    for participante in thread.all_participants:
        try:
            usuario_id = participante.id

            await client.change_nickname(
                grupo,
                usuario_id,
                apodo
            )

            print(
                f"✅ Apodo cambiado a {participante.name}"
            )

            await asyncio.sleep(2)

        except Exception as e:
            print(
                "ocurrio un error:",
                e
            )

    print()
    print("👂 Escuchando cambios de apodos...")
    print(f"📌 Apodo obligatorio: {apodo}")

    # Mantener vivo sin while True
    await asyncio.Event().wait()


asyncio.run(bot())
