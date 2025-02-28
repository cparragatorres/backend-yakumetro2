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

def obtener_consumo_mensual(numero_conexion: str):
    """Consulta el consumo de los últimos 5 meses para el código de conexión"""
    conn = get_db()
    if not conn:
        print("❌ No se pudo conectar a la base de datos")
        return None

    try:
        cursor = conn.cursor()

        query = '''
        SELECT nummes, ROUND(imtotal, 1) AS imtotal_redondeado
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
            consumo_mensual = []
            promedio = round(sum(r[1] for r in results) / len(results), 2)  # Calcular promedio una vez

            for result in results:
                mes = meses.get(result[0], "Mes Desconocido")  # Mapear el mes
                consumo = result[1]

                # Aseguramos que el consumo tenga siempre 2 decimales
                consumo_formateado = float(f"{consumo:.2f}")

                consumo_mensual.append({
                    "mes": mes,
                    "consumo": consumo_formateado,
                    "promedio": promedio
                })

            consumo_mensual = consumo_mensual[::-1]  # Invertimos el orden de los meses
            print(f"🔍 Consumo mensual procesado: {consumo_mensual}")
            return consumo_mensual
        else:
            print("❌ No se encontraron resultados para la consulta")
            return None

    except Exception as e:
        print(f"⚠️ Error durante la consulta: {e}")  # Mostrar errores en consola
        return None
