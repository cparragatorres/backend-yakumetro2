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

def obtener_volumen_facturado(numero_conexion: str):
  conn = get_db()
  if not conn:
    print("❌ No se pudo conectar a la base de datos")  # Mensaje en consola
    return None

  try:
    cursor = conn.cursor()

    query = '''
    SELECT nummes, volfac
    FROM ep26_24_base_codcon
    WHERE CODCON = :1
    ORDER BY NUMMES DESC
    FETCH FIRST 6 ROW ONLY
    '''

    cursor.execute(query, [numero_conexion])
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    if results:
      volumen_mensual = []
      promedio = round(sum(r[1] for r in results) / len(results), 2)  # Calcular promedio una vez

      for result in results:
        mes = meses.get(result[0], "Mes Desconocido")  # Mapear el mes
        volumen = result[1]

        # Aseguramos que el consumo tenga siempre 2 decimales
        volumen_facturado = float(f"{volumen:.2f}")

        volumen_mensual.append({
            "mes": mes,
            "volumen_facturado": volumen_facturado,
            "promedio": promedio
        })

      volumen_mensual = volumen_mensual[::-1]  # Invertimos el orden de los meses
      print(f"🔍 Volumen mensual procesado: {volumen_mensual}")
      return volumen_mensual
    else:
        print("❌ No se encontraron resultados para la consulta")
        return None  # Retorna None si no hay datos

  except Exception as e:
    print(f"⚠️ Error durante la consulta: {e}")  # Mostrar errores en consola
    return None