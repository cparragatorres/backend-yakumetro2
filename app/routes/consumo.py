from fastapi import APIRouter, HTTPException
from app.services.consumo import obtener_consumo

router = APIRouter()

@router.get("/consumo/{numero_conexion}")
def get_consumo(numero_conexion: str):
    result = obtener_consumo(numero_conexion)

    if result is None:
        raise HTTPException(status_code=404, detail="No se encontró el consumo")

    return {"numero_conexion": numero_conexion, "datos": result}
