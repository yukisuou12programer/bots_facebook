import asyncio
from fbchat_v2 import dataGetHome, FileSessionStorage
from fbchat_v2._features._thread import _changeNameThread


async def bot():
    print("YUKI CAMBIADOR DE NOMBRES DEL GRUPO")

    storage = FileSessionStorage("fbchat_v2.json")

    print("🔐 Iniciando sesión...")
    data = await dataGetHome(storage=storage)

    if not data:
        print("❌ No se pudo iniciar sesión.")
        return

    print("✅ Sesión iniciada")

    grupo = input("Escribe la ID del grupo: ").strip()
    nuevo_nombre = input("Escribe el nuevo nombre: ").strip()

    print("\n👀 Cambiando nombre...\n")

    while True:
        try:
            resultado = await _changeNameThread.func(
                data,
                grupo,
                nuevo_nombre
            )

            print(resultado)

            await asyncio.sleep(3)

        except Exception as e:
            print("❌ Ocurrió un error:", e)

            if "rate limit" in str(e).lower():
                print("⏳ Facebook limitó temporalmente las peticiones.")
                await asyncio.sleep(60)

            else:
                await asyncio.sleep(10)


asyncio.run(bot())
