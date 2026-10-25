from fbchat_muqit import Client
import asyncio

client = None
grupo = None
mensaje = None

# ID de tu cuenta
MI_ID = "61594331136087"

# Mensajes ya procesados
mensajes_respondidos = set()


async def on_message(event_data):
    try:
        # Solo este grupo
        if str(event_data.thread_id) != grupo:
            return

        # IGNORAR mensajes enviados por el propio bot
        if str(event_data.sender_id) == MI_ID:
            print("Ignorando mi propio mensaje")
            return

        # ID único del mensaje
        message_id = event_data.id

        # Evitar duplicados
        if message_id in mensajes_respondidos:
            return

        mensajes_respondidos.add(message_id)

        print(
            f"Mensaje recibido de {event_data.sender_id}: "
            f"{event_data.text}"
        )

        await client.send_message(
            mensaje,
            event_data.thread_id
        )
    
        print("✅ Respuesta enviada")

        await asyncio.sleep(8)
        
    except Exception as e:
        print("❌ Error:", e)


async def bot():
    global client, grupo, mensaje

    print("BOT AUTORESPONDEDOR YUKI CHAD")

    client = Client(cookies_file_path="prueba2.json")

    await client.start()

    grupo = input("Escribe la ID del grupo: ").strip()
    mensaje = input("Escribe el mensaje automático: ").strip()

    client.event(on_message)

    print("Escuchando mensajes...")
    print("Responderá a todos los miembros")
    print("Ignorará sus propios mensajes")

    tarea1 =  asyncio.create_task(client.start_listening())
    await tarea1

    await asyncio.Event().wait()


asyncio.run(bot())
