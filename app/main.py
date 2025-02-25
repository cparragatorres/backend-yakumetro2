# backend/app/main.py

from fastapi import FastAPI
from app.routes import importe_por_codigo_routes

app = FastAPI()

# Incluir la ruta de importe por código
app.include_router(importe_por_codigo_routes.router)
