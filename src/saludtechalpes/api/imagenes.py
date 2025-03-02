import saludtechalpes.seedwork.presentacion.api as api
from flask import request, jsonify
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
from saludtechalpes.modulos.imagenes.aplicacion.queries.obtener_imagenes_medicas import ObtenerImagenes
from saludtechalpes.modulos.imagenes.aplicacion.mapeadores import MapeadorImagenDTOJson
from saludtechalpes.modulos.imagenes.infraestructura.despachadores import Despachador
bp = api.crear_blueprint('imagenes', '/imagenes')

@bp.route("/obtener-imagenes", methods=["GET"])
def obtener_imagenes(id = 1):
    pass