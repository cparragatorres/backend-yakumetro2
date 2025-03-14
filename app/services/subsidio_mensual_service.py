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
    """Consulta el consumo de los últimos 6 meses para el código de conexión"""
    conn = get_db()
    if not conn:
        print("❌ No se pudo conectar a la base de datos")
        return None

    try:
        cursor = conn.cursor()

        # Consulta: obtener consumo (IMTOTAL) para los últimos 6 meses
        consulta = '''
        SELECT
            nummes,
            ROUND(volfac, 1) AS volfac_redondeado
        FROM ep26_24_base_codcon
        WHERE codcon = :codcon
        ORDER BY nummes DESC
        FETCH FIRST 6 ROW ONLY
        '''
        cursor.execute(consulta, {"codcon": numero_conexion})
        consumo_results = cursor.fetchall()  # Obtener los resultados de consumo de los 6 últimos meses

        # Consulta: obtener subsidio para los últimos 6 meses
        consulta2 = '''
        SELECT nummes, situdu as SUBSIDIO
            FROM ep26_24_base_codcon
            WHERE codcon = :codcon
            ORDER BY nummes DESC
            FETCH FIRST 6 ROW ONLY
        '''
        cursor.execute(consulta2, {"codcon": numero_conexion})
        subsidio_results = cursor.fetchall()  # Obtener los resultados del subsidio

        # Consulta: obtener el promedio por distrito
        consulta3 = '''
        WITH DistritoPromedio AS (
            SELECT
                *
            FROM ep26_24_base_codcon b
            JOIN ep26_24_geografica_codcon g
                ON b.codcon = g.codcon
            WHERE  coddis in (select coddis from ep26_24_geografica_codcon where codcon = :codcon) AND situdu = 1
        )
        SELECT nummes,
            ROUND(AVG(volfac), 1) AS prom_subsidio_distrito_imtotal_redondeado
            FROM DistritoPromedio
            GROUP BY nummes
            ORDER BY nummes DESC
            FETCH FIRST 6 ROW ONLY
        '''
        cursor.execute(consulta3, {"codcon": numero_conexion})
        promedio_results = cursor.fetchall()  # Obtener los resultados del promedio por distrito

        cursor.close()
        conn.close()

        # Si los resultados existen, combinamos los datos
        if consumo_results and promedio_results and subsidio_results:
            consumo_subsidio = []

            # Creamos un diccionario para combinar los resultados
            for consumo, promedio, subsidio in zip(consumo_results, promedio_results, subsidio_results):
                mes = meses.get(consumo[0], "Mes Desconocido")  # Mapear el mes
                consumo_formateado = float(f"{consumo[1]:.2f}")
                promedio_formateado = float(f"{promedio[1]:.2f}")
                subsidio_value = subsidio[1]  # Obtener el subsidio para este mes

                consumo_subsidio.append({
                    "mes": mes,
                    "promedio": promedio_formateado,
                    "consumo": consumo_formateado,
                    "subsidio": subsidio_value,
                })

            consumo_subsidio = consumo_subsidio[::-1]  # Invertimos el orden de los meses para mostrar de más antiguo a más reciente
            print(f"🔍 Consumo distrito procesado: {consumo_subsidio}")
            return consumo_subsidio
        else:
            print("❌ No se encontraron resultados para las consultas")
            return None

    except Exception as e:
        print(f"⚠️ Error durante la consulta: {e}")  # Mostrar errores en consola
        return None
