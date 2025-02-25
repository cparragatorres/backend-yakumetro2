# backend/app/routes/importe_por_codigo_routes.py

from fastapi import APIRouter, HTTPException
from app.services.importe_por_codigo_service import obtener_importe_por_codigo

router = APIRouter()

@router.get("/ultimo-importe-total/{numero_conexion}")
def get_importe(numero_conexion: str):
    result = obtener_importe_por_codigo(numero_conexion)

    if result is None:
        raise HTTPException(status_code=404, detail="No se encontró el importe para el código")

    return {
        "numero_conexion": numero_conexion,
        "imtotal": result[0]
    }
