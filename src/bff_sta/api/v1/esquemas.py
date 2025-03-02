import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


EXPORTACION_STA_HOST = os.getenv("EXPORTACION_STA_ADDRESS", default="exportacionsta")

def obtener_imagenes(root) -> int:
    response = requests.get(f'http://{EXPORTACION_STA_HOST}:5001/exportar')
    
    if response.status_code in [200, 202]:
        return 202
    else:
        response.raise_for_status()

    