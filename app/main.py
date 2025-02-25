# backend/app/main.py

from fastapi import FastAPI
from app.routes import importe_por_codigo_routes
from app.routes import volumen_facturado_routes
from app.routes import medidor_existe_routes
from app.routes import subsidio_existe_routes

app = FastAPI()

# Incluir la ruta de importe por código
app.include_router(importe_por_codigo_routes.router)
app.include_router(volumen_facturado_routes.router)
app.include_router(medidor_existe_routes.router)
app.include_router(subsidio_existe_routes.router)
