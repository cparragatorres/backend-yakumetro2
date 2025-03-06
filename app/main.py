from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar todas las rutas
from app.routes import (
    importe_por_codigo_routes,
    subsidio_mensual_routes,
    volumen_facturado_routes,
    modalidad_facturacion_routes,
    subsidio_existe_routes,
    consumo_mensual_routes,
    consumo_distrito_routes
)

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

# Incluir rutas de la API
app.include_router(importe_por_codigo_routes.router)
app.include_router(volumen_facturado_routes.router)
app.include_router(modalidad_facturacion_routes.router)
app.include_router(subsidio_existe_routes.router)
app.include_router(consumo_mensual_routes.router)
app.include_router(consumo_distrito_routes.router)
app.include_router(subsidio_mensual_routes.router)
