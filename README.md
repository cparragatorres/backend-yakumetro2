# Yakumetro2 - Backend

## Descripción
Este es el backend de Yakumetro2, una aplicación que permite a los usuarios consultar su consumo de agua potable.
Se conecta a una base de datos Oracle de manera remota y proporciona datos a un frontend en React.

## Tecnologías utilizadas
- **FastAPI**: Framework para construir la API REST.
- **Uvicorn**: Servidor ASGI para ejecutar la aplicación.
- **cx_Oracle**: Cliente de Oracle para conectar con la base de datos.
- **SQLAlchemy**: ORM opcional para manejar la base de datos.
- **Python-dotenv**: Para cargar variables de entorno desde un archivo `.env`.
- **Pydantic**: Validación de datos y modelos de respuesta.
- **CORS**: Para permitir el acceso del frontend.

## Estructura del proyecto
```
backend/
│── app/
│   ├── core/
│   │   ├── config.py   # Configuración de variables de entorno
│   ├── routes/         # Endpoints de la API
│   ├── models/         # Modelos de la base de datos
│   ├── services/       # Lógica de negocio y consultas a la base de datos
│   ├── config.py    # Carga variables de entorno
│   ├── models.py    # Modelos de base de datos (si se usa SQLAlchemy)
│   ├── routes/
│   │   ├── consumo.py  # Endpoints de consumo de agua
│   │   ├── usuario.py  # Endpoints de usuarios
│   ├── services/
│   │   ├── database.py  # Configuración de la BD
│   │   ├── consumo_service.py  # Lógica del negocio
│   │   ├── usuario_service.py  # Lógica de usuarios
│   ├── schemas/
│   │   ├── consumo_schema.py  # Esquema de validación de consumo
│   │   ├── usuario_schema.py  # Esquema de validación de usuario
│── main.py             # Punto de entrada de FastAPI
│-- .env           # Variables de entorno
│-- requirements.txt  # Dependencias
│── .gitignore          # Archivos a ignorar en Git
│-- README.md     # Documentación del backend
```

## Instalación y Configuración
### 1. Crear el entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Configurar variables de entorno
Crea un archivo `.env` en la carpeta `backend/` con la siguiente estructura:
```ini
DATABASE_USER=tu_usuario
DATABASE_PASSWORD=tu_contraseña
DATABASE_HOST=tu_host
DATABASE_PORT=1521
DATABASE_SERVICE_NAME=tu_servicio
DATABASE_DSN=(DESCRIPTION=(ADDRESS=(PROTOCOL=TCP)(HOST=${DATABASE_HOST})(PORT=${DATABASE_PORT}))(CONNECT_DATA=(SERVICE_NAME=${DATABASE_SERVICE_NAME})))
```

### 4. Ejecutar el backend
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

El backend estará disponible en `http://127.0.0.1:8000`

## 📌 Notas
- El archivo `.env` debe contener las credenciales sensibles y no debe subirse a GitHub.
- `config.py` maneja la configuración y las variables de entorno.
- Se recomienda trabajar con `virtualenv` para evitar conflictos entre dependencias.

## 📡 Despliegue
Para desplegar este backend en un servidor, se pueden seguir estas opciones:

- Usar **Docker** para contenerizar la aplicación.
- Desplegar en **Railway, Render, AWS, o cualquier proveedor cloud**.

## Endpoints disponibles
- **`GET /consumo/{numero_suministro}`** → Devuelve el consumo de agua del usuario.
- **`GET /consumo/vecindario/{numero_suministro}`** → Compara el consumo con el promedio de la manzana.
- **`GET /consumo/distrito/{numero_suministro}`** → Compara el consumo con el promedio del distrito.

## Futuras mejoras
✅ Integración con autenticación mediante JWT
✅ Implementar caché para mejorar el rendimiento en consultas grandes
✅ Optimizar las consultas a la base de datos Oracle
