import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


EXPORTACION_STA_HOST = os.getenv("EXPORTACION_STA_ADDRESS", default="localhost")
EXPORTACION_STA_PORT = os.getenv("EXPORTACION_STA_PORT", default="5000")

def obtener_imagenes(root, tipo_patologia: str, tipo_imagen: str):
    url = f'http://{EXPORTACION_STA_HOST}:{EXPORTACION_STA_PORT}/exportar'
    headers = {'Content-Type': 'application/json'}
    data = {
        "tipo_patologia": tipo_patologia,
        "tipo_imagen": tipo_imagen
    }
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code in [200, 202]:
        return StatusResponse(status_code=response.status_code)
    else:
        response.raise_for_status()

@strawberry.type
class Imagen:
    tipo_patologia: str
    tipo_imagen : str

@strawberry.type
class StatusResponse:
    status_code: int    