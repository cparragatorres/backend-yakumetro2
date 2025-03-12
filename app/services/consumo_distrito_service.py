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

def obtener_consumo_distrito(numero_conexion: str):
    """Consulta el consumo de los últimos 6 meses para el código de conexión"""
    conn = get_db()
    if not conn:
        print("❌ No se pudo conectar a la base de datos")
        return None

    try:
        cursor = conn.cursor()

        # Primera consulta: obtener CODDIS para el CODCON
        consulta1 = '''
        SELECT CODDIS
        FROM EP26_24_GEOGRAFICA_CODCON
        WHERE CODCON = :codcon
        '''

        cursor.execute(consulta1, {"codcon": numero_conexion})
        coddis_result = cursor.fetchone()  # Obtener el resultado de la primera consulta
        if not coddis_result:
            print("❌ No se encontró CODDIS para el código de conexión")
            return None

        coddis_value = coddis_result[0]  # Guardamos el valor de CODDIS

        # Segunda consulta: obtener consumo (IMTOTAL) y el promedio por distrito
        consulta2 = '''
        SELECT
            nummes,
            ROUND(imtotal, 1) AS imtotal_redondeado
        FROM ep26_24_base_codcon
        WHERE codcon = :codcon
        ORDER BY nummes DESC
        FETCH FIRST 6 ROW ONLY
        '''

        cursor.execute(consulta2, {"codcon": numero_conexion})
        consumo_results = cursor.fetchall()  # Obtener los resultados de consumo de los 6 últimos meses

        # Tercera consulta: obtener el promedio por distrito
        consulta3 = '''
        WITH DistritoPromedio AS (
            SELECT
                b.nummes,
                ROUND(AVG(b.imtotal), 1) AS prom_distrito_imtotal_redondeado
            FROM ep26_24_base_codcon b
            JOIN ep26_24_geografica_codcon g ON b.codcon = g.codcon
            WHERE g.coddis = :coddis
            GROUP BY b.nummes
        )
        SELECT
            nummes,
            prom_distrito_imtotal_redondeado
        FROM DistritoPromedio
        ORDER BY nummes DESC
        FETCH FIRST 6 ROWS ONLY
        '''

        cursor.execute(consulta3, {"coddis": coddis_value})
        promedio_results = cursor.fetchall()  # Obtener los resultados del promedio por distrito

        cursor.close()
        conn.close()

        # Si ambos resultados existen, combinamos los datos
        if consumo_results and promedio_results:
            consumo_distrito = []

            # Creamos un diccionario para combinar los resultados
            for consumo, promedio in zip(consumo_results, promedio_results):
                mes = meses.get(consumo[0], "Mes Desconocido")  # Mapear el mes
                consumo_formateado = float(f"{consumo[1]:.2f}")
                promedio_formateado = float(f"{promedio[1]:.2f}")

                consumo_distrito.append({
                    "mes": mes,
                    "promedio": promedio_formateado,
                    "consumo": consumo_formateado
                })

            consumo_distrito = consumo_distrito[::-1]  # Invertimos el orden de los meses para mostrar de más antiguo a más reciente
            print(f"🔍 Consumo distrito procesado: {consumo_distrito}")
            return consumo_distrito
        else:
            print("❌ No se encontraron resultados para las consultas")
            return None

    except Exception as e:
        print(f"⚠️ Error durante la consulta: {e}")  # Mostrar errores en consola
        return None
