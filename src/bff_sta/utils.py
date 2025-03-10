import time
import os
import datetime
import requests
import json
from fastavro.schema import parse_schema
from pulsar.schema import *

epoch = datetime.datetime.utcfromtimestamp(0)
PULSAR_ENV: str = 'BROKER_HOST'

def time_millis():
    return int(time.time() * 1000)

def unix_time_millis(dt):
    return (dt - epoch).total_seconds() * 1000.0

def millis_a_datetime(millis):
    return datetime.datetime.fromtimestamp(millis/1000.0)

def broker_host():
    return os.getenv(PULSAR_ENV, default="localhost")

def consultar_schema_registry(topico: str) -> dict:
    response = requests.get(f'http://{broker_host()}:8080/admin/v2/schemas/{topico}/schema')
    response.raise_for_status()  # Esto lanzará una excepción para códigos de estado HTTP 4xx/5xx
    json_registry = response.json()
    return json_registry.get('data', {})

def obtener_schema_avro_de_diccionario(json_schema: dict | str) -> AvroSchema:
    try:
        # Si json_schema es un string, parsearlo a diccionario
        if isinstance(json_schema, str):
            json_schema = json.loads(json_schema)

        if "type" not in json_schema or json_schema["type"] != "record":
            raise ValueError(f"El esquema obtenido no es un esquema Avro válido: {json_schema}")

        # Extraer registros anidados
        tipos_referenciados = []
        for field in json_schema.get("fields", []):
            if isinstance(field["type"], dict) and field["type"].get("type") == "record":
                record_def = field["type"]
                tipos_referenciados.append(record_def)
                field["type"] = record_def["name"]

        schema_completo = [json_schema] + tipos_referenciados

        # Pasar el esquema corregido a fastavro
        definicion_schema = parse_schema(schema_completo)
        return AvroSchema(None, schema_definition=definicion_schema)

    except Exception as e:
        raise ValueError(f"Error procesando el esquema Avro: {e}, esquema: {json_schema}")
