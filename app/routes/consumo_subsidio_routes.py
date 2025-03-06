from fastapi import APIRouter, HTTPException
from app.services.consumo_subsidio_service import obtener_subsidio_mensual

router = APIRouter()

@router.get("/subsidio-mensual/{numero_conexion}")
def get_subsidio_mensual(numero_conexion: str):
    """Devuelve los datos de subsidio mensual para el código de conexión"""
    subsidio_mensual = obtener_subsidio_mensual(numero_conexion)

    if subsidio_mensual is None:
        raise HTTPException(status_code=404, detail="No se encontraron datos de subsidio mensual")

    return subsidio_mensual
