# backend/app/routes/medidor_existe_routes.py

from fastapi import APIRouter, HTTPException
from app.services.modalidad_facturacion_service import verificar_medidor

router = APIRouter()

@router.get("/medidor-existe/{numero_conexion}")
def get_medidor(numero_conexion: str):
    """Devuelve 1 si el código de conexión tiene medidor, 0 si no tiene."""
    result = verificar_medidor(numero_conexion)

    if result is None:
        raise HTTPException(status_code=404, detail="No se logró consultar si tiene medidor o no")

    return {
        "numero_conexion": numero_conexion,
        "modalidad_facturacion": result
    }
