from app.core.database import get_db

# Diccionario para mapear los números de mes
meses = {
    12: "Diciembre",
    11: "Noviembre",
    10: "Octubre",
    9: "Septiembre",
    8: "Agosto",
    7: "Julio",
}

def obtener_subsidio_mensual(numero_conexion: str):
    """Consulta si tuvo subsidio en los últimos 6 meses para el código de conexión"""
    conn = get_db()
    if not conn:
        print("❌ No se pudo conectar a la base de datos")
        return None

    try:
        cursor = conn.cursor()

        query = '''
        SELECT nummes, situdu as SUBSIDIO
        FROM ep26_24_base_codcon
        WHERE codcon = :1
        ORDER BY nummes DESC
        FETCH FIRST 6 ROW ONLY
        '''

        cursor.execute(query, [numero_conexion])
        results = cursor.fetchall()  # Obtener los resultados de los 5 últimos meses
        print(f"🔍 Resultados obtenidos: {results}")

        cursor.close()
        conn.close()

        # Si los resultados existen, procesamos los datos
        if results:
            subsidio_mensual = []

            for result in results:
                mes = meses.get(result[0], "Mes Desconocido")  # Mapear el mes
                subsidio = result[1]

                subsidio_mensual.append({
                    "mes": mes,
                    "subsidio": subsidio,
                })

            subsidio_mensual = subsidio_mensual[::-1]  # Invertimos el orden de los meses
            print(f"🔍 Subsidio mensual procesado: {subsidio_mensual}")
            return subsidio_mensual
        else:
            print("❌ No se encontraron resultados para la consulta")
            return None

    except Exception as e:
        print(f"⚠️ Error durante la consulta: {e}")  # Mostrar errores en consola
        return None
