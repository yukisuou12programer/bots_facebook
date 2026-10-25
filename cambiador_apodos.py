from fbchat_muqit import Client
import asyncio

async def bot():
   client = Client(cookies_file_path="prueba2.json")
   await client.start()
   grupo = input("escribe la id del grupo: ").strip()
   #apodo = input("escribe apodo a poner: ")

   asyncio.create_task(client.start_listening())
   await asyncio.sleep(2)

   threads = await client.fetch_thread_info([grupo])
   if not threads:
      print("no se encontro grupo")

   thread = threads[0]

   print(f"Nombre del grupo {thread.name}")
   print("participantes encontrados:",len(thread.all_participants))

   print("informacion del grupo: \n")

   while True:
       for participante in thread.all_participants:
           try:
              usuario_id = participante.id

              await client.change_nickname(grupo,usuario_id,"")
              print(f"apodo cambiado a {participante.name}")
              await asyncio.sleep(2)
           except Exception as e:
              print("ocurrio un error:",e)

asyncio.run(bot())
