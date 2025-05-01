from fastapi import FastAPI
from .routes.endpoints import router

app = FastAPI()
app.title = "Calificaciones"
app.include_router(router=router)

@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}
    