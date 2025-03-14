from fastapi import APIRouter, HTTPException
from app.services.consumo_manzana_service import obtener_manzana_mensual

router = APIRouter()

@router.get("/consumo-manzana/{numero_conexion}")
def get_consumo_manzana(numero_conexion: str):
    """Devuelve los datos de consumo manzana para el código de conexión"""
    consumo_manzana = obtener_manzana_mensual(numero_conexion)

    if consumo_manzana is None:
        raise HTTPException(status_code=404, detail="No se encontraron datos de consumo manzana")

    return consumo_manzana
