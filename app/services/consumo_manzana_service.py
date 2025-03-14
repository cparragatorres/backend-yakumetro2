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

def obtener_manzana_mensual(numero_conexion: str):
    """Consulta el consumo de los últimos 6 meses para  el código de conexión"""
    conn = get_db()
    if not conn:
        print("❌ No se pudo conectar a la base de datos")
        return None

    try:
        cursor = conn.cursor()

        # Se esta usando VOLFAC en lugar de IMTOTAL
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

        # Se está usando VOLFAC en lugar de IMTOTAL
        consulta2 = '''
        WITH ManzanaPromedio AS (
                SELECT
                b.codcon,
                m.codman,
                b.nummes,
                b.volfac
                FROM ep26_24_base_codcon b
                JOIN ep26_24_manzanas_codcon m
                    ON b.codcon = m.codcon
                WHERE codman IN (select codman from ep26_24_manzanas_codcon where codcon = :codcon)
            )
        SELECT nummes,
            ROUND(AVG(volfac), 1) AS prom_volfac_manzana_redondeado
            FROM ManzanaPromedio
            GROUP BY nummes
            ORDER BY nummes DESC
            FETCH FIRST 6 ROW ONLY
        '''

        cursor.execute(consulta2, {"codcon": numero_conexion})
        promedio_results = cursor.fetchall()  # Obtener los resultados del promedio por manzana

        cursor.close()
        conn.close()

        # Si ambos resultados existen, combinamos los datos
        if consumo_results and promedio_results:
            consumo_manzana = []

            # Creamos un diccionario para combinar los resultados
            for consumo, promedio in zip(consumo_results, promedio_results):
                mes = meses.get(consumo[0], "Mes Desconocido")  # Mapear el mes
                consumo_formateado = float(f"{consumo[1]:.2f}")
                promedio_formateado = float(f"{promedio[1]:.2f}")

                consumo_manzana.append({
                    "mes": mes,
                    "promedio": promedio_formateado,
                    "consumo": consumo_formateado
                })

            consumo_manzana = consumo_manzana[::-1]  # Invertimos el orden de los meses para mostrar de más antiguo a más reciente
            print(f"🔍 Consumo manzana procesado: {consumo_manzana}")
            return consumo_manzana
        else:
            print("❌ No se encontraron resultados para las consultas")
            return None

    except Exception as e:
        print(f"⚠️ Error durante la consulta: {e}")  # Mostrar errores en consola
        return None
