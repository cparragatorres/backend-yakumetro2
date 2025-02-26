from app.core.database import get_db

def obtener_volumen_facturado(numero_conexion: str):
  conn = get_db()
  if not conn:
    print("❌ No se pudo conectar a la base de datos")  # Mensaje en consola
    return None

  try:
    cursor = conn.cursor()

    query = '''
    SELECT VOLFAC
    FROM ep26_24_base_codcon
    WHERE CODCON = :1
    ORDER BY NUMMES DESC
    FETCH FIRST 1 ROW ONLY
    '''

    cursor.execute(query, [numero_conexion])
    result = cursor.fetchone()
    cursor.close()
    conn.close()

    print(f"🔍 Volumen facturado encontrado: {result}")  # Para ver en la consola
    return result if result else "0"  # Retorna None si no hay datos
  except Exception as e:
    print(f"⚠️ Error durante la consulta: {e}")  # Mostrar errores en consola
    return None