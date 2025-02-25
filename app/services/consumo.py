# backend/app/services/consumo.py

from app.core.database import get_db
from datetime import datetime

def obtener_consumo(numero_conexion: str):
    conn = get_db()
    if not conn:
        print("No se pudo conectar a la base de datos")  # Mensaje en consola
        return None

    try:
        cursor = conn.cursor()

        # Obtener el mes actual
        mes_actual = datetime.now().month

        # Consulta parametrizada para evitar inyección SQL
        query = '''
        SELECT imtotal
        FROM ep26_23_base_codcon
        WHERE codcon = :1
        AND nuanio = 2023
        AND nummes = :2
        '''

        cursor.execute(query, [numero_conexion, mes_actual])
        result = cursor.fetchone()
        cursor.close()
        conn.close()

        print(f"Resultado de la consulta para el mes {mes_actual}: {result}")  # Para ver el resultado en consola
        return result if result else None  # Retorna None si no hay datos
    except Exception as e:
        print(f"Error durante la consulta: {e}")  # Mostrar errores en consola
        return None
