# backend/app/services/medidor_existe_service.py

from app.core.database import get_db

def verificar_medidor(numero_conexion: str):
    """Consulta si el código de conexión tiene medidor o no."""
    conn = get_db()
    if not conn:
        print("❌ No se pudo conectar a la base de datos")
        return None

    try:
        cursor = conn.cursor()

        # Consulta para obtener el último CODMOF para el código de conexión
        query = '''
        SELECT CODMOF
        FROM ep26_24_base_codudu
        WHERE codcon = :1
        ORDER BY nummes DESC
        FETCH FIRST 1 ROW ONLY
        '''

        cursor.execute(query, [numero_conexion])
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        # Si el resultado es None o NULL, retorna 0 (False)
        if result is None or result[0] is None:
            print(f"🔍 Resultado: NULL (sin medidor) -> Retornando 0")
            return 0  # O podrías retornar False o "sin medidor"

        print(f"🔍 Resultado: {result[0]} (con medidor) -> Retornando 1")
        return 1  # O podrías retornar True
    except Exception as e:
        print(f"⚠️ Error durante la consulta: {e}")
        return None
