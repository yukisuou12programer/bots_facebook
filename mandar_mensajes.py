from fbchat_muqit import Client
import asyncio

async def bot():
    client = Client(cookies_file_path="prueba.json")
    await client.start()
    mensajes = ["vamos","burla","solo","das",
               "pena","sos la burla","das risa",
               "no sabes defenderte","gordo puto"]
               
    grupo = input("escribe id del grupo: ").strip()
    asyncio.create_task(client.start_listening())
    
    while True:
       try:
          for texto in mensajes:
              await client.send_message(texto,grupo)
              print("mensaje enviado")
              await asyncio.sleep(1)
       except Exception as e:
              print("ocurrio un error:",e)

              if "Message queue full" in str(e):
                  print("La cola está llena. Esperando 40 segundos...")
                  await asyncio.sleep(40)
       
asyncio.run(bot())
