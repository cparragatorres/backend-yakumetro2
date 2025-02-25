from fastapi import FastAPI
from app.routes import consumo

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Yakumetro2 Backend is running 🚀"}

# Incluir las rutas de consumo
app.include_router(consumo.router)
