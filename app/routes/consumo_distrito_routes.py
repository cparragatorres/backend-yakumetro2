from fastapi import APIRouter, HTTPException
from app.services.consumo_distrito_service import obtener_consumo_distrito

router = APIRouter()

@router.get("/consumo-distrito/{numero_conexion}")
def get_consumo_distrito(numero_conexion: str):
    """Devuelve los datos de consumo distrito para el código de conexión"""
    consumo_distrito = obtener_consumo_distrito(numero_conexion)

    if consumo_distrito is None:
        raise HTTPException(status_code=404, detail="No se encontraron datos de consumo distrito")

    return consumo_distrito
