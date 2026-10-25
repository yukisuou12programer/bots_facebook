from fbchat_muqit import Client
import asyncio

async def bot_hecho():
    print("YUKI CAMBIADOR DE NOMBRES DEL GRUPO")
    
    client = Client(cookies_file_path="prueba2.json")

    await client.start()

    grupo = input("Escribe la ID del grupo: ").strip()
    nuevo_nombre = input("Escribe el nuevo nombre: ")

    asyncio.create_task(client.start_listening())

    while True:
          try:
              await client.change_thread_name(grupo, nuevo_nombre)
              print("Nombre cambiado exitosamente")
              await asyncio.sleep(4)
          except Exception as e:
               print("ocurrio error:", e)

               if "Message queue full" in str(e):
                   print("La cola está llena. Esperando 40 segundos...")
                   await asyncio.sleep(40)

asyncio.run(bot_hecho())
