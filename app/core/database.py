# backend/app/core/database.py

import os
import oracledb
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Obtener variables de entorno
DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = os.getenv("DATABASE_PORT")
DB_SERVICE_NAME = os.getenv("DATABASE_SERVICE_NAME")

# Crear DSN para la conexión
dsn = f"(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST={DB_HOST})(PORT={DB_PORT}))(CONNECT_DATA=(SERVICE_NAME={DB_SERVICE_NAME})))"

# Función para obtener una conexión a la base de datos
def get_db():
    try:
        conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=dsn)
        return conn
    except oracledb.DatabaseError as e:
        print("Error al conectar con la base de datos:", e)
        return None
