import os
from app.core.config import settings
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

# Configuración de la base de datos
DATABASE_USER = os.getenv("DATABASE_USER")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
DATABASE_HOST = os.getenv("DATABASE_HOST")
DATABASE_PORT = os.getenv("DATABASE_PORT")
DATABASE_SERVICE_NAME = os.getenv("DATABASE_SERVICE_NAME")
DATABASE_DSN = os.getenv("DATABASE_DSN")
