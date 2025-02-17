from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Yakumetro2 Backend is running 🚀"}
