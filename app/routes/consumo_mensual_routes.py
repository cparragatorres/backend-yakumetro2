# backend/app/routes/consumo_mensual_routes.py

from fastapi import APIRouter, HTTPException
from app.services.consumo_mensual_service import obtener_consumo_mensual

router = APIRouter()

@router.get("/consumo-mensual/{numero_conexion}")
def get_consumo_mensual(numero_conexion: str):
    """Devuelve los datos de consumo mensual para el código de conexión"""
    consumo_mensual = obtener_consumo_mensual(numero_conexion)

    if consumo_mensual is None:
        raise HTTPException(status_code=404, detail="No se encontraron datos de consumo mensual")

    return consumo_mensual
