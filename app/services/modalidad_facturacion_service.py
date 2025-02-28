from app.core.database import get_db

def verificar_medidor(numero_conexion: str):
    """Consulta si el código de conexión tiene medidor o no y devuelve la modalidad."""
    conn = get_db()
    if not conn:
        print("❌ No se pudo conectar a la base de datos")
        return None

    try:
        cursor = conn.cursor()

        # Consulta para obtener el último NOMCAT para el código de conexión
        query = '''
        SELECT NOMCAT
        FROM ep26_24_base_codudu
        WHERE codcon = :1
        ORDER BY nummes DESC
        FETCH FIRST 6 ROW ONLY
        '''

        cursor.execute(query, [numero_conexion])
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        # Si el resultado es None o NULL, retorna "SIN MODALIDAD"
        if result is None or result[0] is None:
            print(f"🔍 Resultado: NULL (sin medidor) -> Retornando 'SIN MODALIDAD'")
            return "SIN MODALIDAD"

        # Usamos match-case para asignar la modalidad según el valor de NOMCAT
        match result[0]:
            case 101:
                modalidad = "SOCIAL"
            case 102:
                modalidad = "DOMESTICO"
            case 103:
                modalidad = "COMERCIAL"
            case 104:
                modalidad = "INDUSTRIAL"
            case 105:
                modalidad = "ESTATAL"
            case _:
                modalidad = "SIN MODALIDAD"  # Si no es ninguno de los casos anteriores

        print(f"🔍 Resultado: {modalidad} -> Retornando modalidad")
        return modalidad

    except Exception as e:
        print(f"⚠️ Error durante la consulta: {e}")
        return None
