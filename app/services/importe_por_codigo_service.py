# backend/app/services/importe_por_codigo_service.py

from app.core.database import get_db

def obtener_importe_por_codigo(numero_conexion: str):
    """Consulta el último importe disponible para un número de conexión"""
    conn = get_db()
    if not conn:
        print("❌ No se pudo conectar a la base de datos")  # Mensaje en consola
        return None

    try:
        cursor = conn.cursor()

        query = '''
        SELECT imtotal
        FROM ep26_24_base_codcon
        WHERE codcon = :1
        ORDER BY nuanio DESC, nummes DESC
        FETCH FIRST 1 ROW ONLY
        '''

        cursor.execute(query, [numero_conexion])
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        print(f"🔍 Último importe encontrado: {result}")  # Para ver en la consola
        return result if result else None  # Retorna None si no hay datos
    except Exception as e:
        print(f"⚠️ Error durante la consulta: {e}")  # Mostrar errores en consola
        return None
