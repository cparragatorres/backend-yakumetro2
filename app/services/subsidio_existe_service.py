# backend/app/routes/subsidio_existe_service.py

from app.core.database import get_db

def verificar_subsidio(numero_conexion: str):
  conn = get_db()
  if not conn:
    print("❌ No se pudo conectar a la base de datos")
    return None

  try:
    cursor = conn.cursor()

    # Consulta para obtener el número de subsidios para el código de conexión
    query = '''
    SELECT SITUDU
    FROM ep26_24_base_codcon
    WHERE codcon = :1
    ORDER BY nummes DESC
    FETCH FIRST 1 ROW ONLY
    '''

    cursor.execute(query, [numero_conexion])
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    print(f"🔍 Conexion con subsidio encontrado: {result}")
    return result if result else None # Retorna None si no hay datos
  except Exception as e:
    print(f"⚠️ Error durante la consulta: {e}")
    return None