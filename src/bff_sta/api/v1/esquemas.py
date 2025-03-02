import typing
import strawberry
import uuid
import requests
import os

from datetime import datetime


EXPORTACION_STA_HOST = os.getenv("EXPORTACION_STA_ADDRESS", default="exportacionsta")
FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

def obtener_imagenes(root) -> typing.List["Imagen"]:
    imagenes_json = requests.get(f'http://{EXPORTACION_STA_HOST}:5000/exportar').json()
    imagenes = []

    for reserva in imagenes_json:
        imagenes.append(
            Imagen(
                tipo_patologia=reserva['tipo_patologia'],
                tipo_imagen=reserva['tipo_imagen']
            )
        )

    return imagenes


@strawberry.type
class Imagen:
    tipo_patologia: str
    tipo_imagen : str 
   
    