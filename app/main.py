from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Importar todas las rutas
from app.routes import (
    importe_por_codigo_routes,
    volumen_facturado_routes,
    modalidad_facturacion_routes,
    subsidio_existe_routes,
    consumo_mensual_routes  # 👈 Verifica que esté bien importado
)

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL del frontend en desarrollo
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los headers
)

# Incluir rutas de la API
app.include_router(importe_por_codigo_routes.router)
app.include_router(volumen_facturado_routes.router)
app.include_router(modalidad_facturacion_routes.router)
app.include_router(subsidio_existe_routes.router)
app.include_router(consumo_mensual_routes.router)  # 👈 Verifica que no haya un error aquí
