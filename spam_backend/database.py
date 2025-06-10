from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Cargar variables del archivo .env

MONGODB_URL = os.getenv("MONGODB_URL")
client = MongoClient(MONGODB_URL)

db = client["detector_llamadas"]  # Nombre de tu base de datos
coleccion_usuarios = db["usuarios"]  # Nombre de tu colección
