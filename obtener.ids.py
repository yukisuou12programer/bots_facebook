from fbchat_muqit import Client
import asyncio

async def bot():
    client = Client(cookies_file_path="prueba2.json")

    await client.start()

    print("\nGRUPOS EN LOS QUE ESTÁS\n")

    threads = await client.fetch_thread_list()

    for thread in threads:
        print("Nombre:", thread.name)
        print("ID:", thread.thread_id)
        print("-" * 30)

asyncio.run(bot())
