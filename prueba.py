import asyncio
from fbchat_v2 import dataGetHome, FileSessionStorage

async def main():
    storage = FileSessionStorage("fbchat_v2.json")

    print("Comprobando sesión de Facebook...")

    data = await dataGetHome(storage=storage)

    if data:
        print("✅ Sesión iniciada correctamente")

        # No mostrar cookies ni datos privados
        print("Se recibieron los datos de sesión.")
    else:
        print("❌ No se pudo iniciar sesión")
        print("Revisa las cookies o vuelve a obtenerlas.")

asyncio.run(main())
