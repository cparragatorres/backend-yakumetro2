# backend/app/services/consumo.py

from app.core.database import get_db

def obtener_consumo(numero_conexion: str):
    conn = get_db()
    if not conn:
        print("❌ No se pudo conectar a la base de datos")  # Mensaje en consola
        return None

    try:
        cursor = conn.cursor()
        query = "SELECT * FROM consumos WHERE numero_conexion = :1"
        cursor.execute(query, [numero_conexion])
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        print(f"🔍 Resultado de la consulta: {result}")  # Para ver el resultado en consola
        return result
    except Exception as e:
        print(f"⚠️ Error durante la consulta: {e}")  # Mostrar errores en consola
        return None
