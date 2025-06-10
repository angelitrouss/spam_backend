from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from database import coleccion_usuarios

app = FastAPI()

# Middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Para pruebas desde Android
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/usuarios")
def verificar_numero(telefono: str = Query(...)):
    usuario = coleccion_usuarios.find_one({"telefono": telefono})
    return {"spam": usuario is not None}
