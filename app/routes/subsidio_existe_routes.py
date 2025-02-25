# backend/app/routes/subsidio_existe_routes.py

from fastapi import APIRouter, HTTPException
from app.services.subsidio_existe_service import verificar_subsidio

router = APIRouter()

@router.get("/subsidio-existe/{numero_conexion}")
def get_subsidio(numero_conexion: str):
  result = verificar_subsidio(numero_conexion)

  if result is None:
    raise HTTPException(status_code=404, detail="No se logró obtener el subsidio para el código de conexión")

  return {
    "numero_conexion": numero_conexion,
    "existe_subsidio": result[0]  # 1 o 0
  }
