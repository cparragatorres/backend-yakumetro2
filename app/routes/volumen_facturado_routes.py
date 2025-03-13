from fastapi import APIRouter, HTTPException
from app.services.volumen_facturado_service import obtener_volumen_facturado

router = APIRouter()

@router.get("/volumen-facturado/{numero_conexion}")
def get_volumen_facturado(numero_conexion: str):
  result = obtener_volumen_facturado(numero_conexion)

  if result is None:
      raise HTTPException(status_code=404, detail="No se encontró el volumen facturado para el código de conexión")

  return {
    "numero_conexion": numero_conexion,
    "volumen_facturado": result
  }