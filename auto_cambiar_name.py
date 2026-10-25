from fbchat_muqit import Client
import asyncio


# ==============================
# CONFIGURACIÓN
# ==============================

GRUPO_ID = input("Escribe el ID del grupo: ").strip()

NOMBRE_CORRECTO = input(
    "Escribe el nombre correcto: "
).strip()


# ==============================
# CREAR CLIENTE
# ==============================

client = Client(
    cookies_file_path="prueba2.json"
)


# ==============================
# EVENTO DE CAMBIO DE NOMBRE
# ==============================

@client.event
async def on_thread_name_change(event_data, message):
    try:

        # Comprobar el grupo
        if str(message.thread_id) != GRUPO_ID:
            return

        print("\n========== CAMBIO DETECTADO ==========")

        print(
            "ID DEL GRUPO:",
            message.thread_id
        )

        print(
            "DATOS DEL EVENTO:",
            event_data
        )

        # Obtener el nombre del evento
        nombre_nuevo = getattr(
            event_data,
            "name",
            None
        )

        print(
            "NUEVO NOMBRE:",
            nombre_nuevo
        )

        # Si ya tiene el nombre correcto
        if nombre_nuevo == NOMBRE_CORRECTO:
            print("✅ El nombre ya es correcto")
            return

        print("🔄 Restaurando nombre...")

        # Cambiar el nombre del grupo
        await client.change_thread_name(
            GRUPO_ID,
            NOMBRE_CORRECTO
        )

        print("✅ Nombre restaurado")

    except Exception as e:

        print(
            "❌ Error en el evento:",
            e
        )


# ==============================
# FUNCIÓN PRINCIPAL
# ==============================

async def main():

    try:

        await client.start()

        print("\n🤖 Bot conectado")
        print("👀 Esperando cambios de nombre...")

        # Iniciar la escucha en segundo plano
        asyncio.create_task(
            client.start_listening()
        )

        # Mantener el programa activo
        await asyncio.Event().wait()

    except KeyboardInterrupt:

        print("\n🛑 Bot detenido")

    except Exception as e:

        print(
            "❌ Error principal:",
            e
        )


# ==============================
# EJECUTAR
# ==============================

asyncio.run(main())
