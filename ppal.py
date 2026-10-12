from fastapi import FastAPI
from rutas import tareas

app = FastAPI(title="api de tareas json")

# conectamos las rutas del otro archivo
app.include_router(tareas.router)

@app.get("/")
def raiz():
    return {"mensaje": "servidor corriendo al 100%, probar en /docs"}
