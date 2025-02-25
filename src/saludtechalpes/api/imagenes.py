import saludtechalpes.seedwork.presentacion.api as api
from flask import request, jsonify
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
from saludtechalpes.modulos.imagenes.aplicacion.queries.obtener_imagenes_medicas import ObtenerImagenes

bp = api.crear_blueprint('imagenes', '/imagenes')

@bp.route("/obtener-imagenes", methods=["GET"])
def obtener_imagenes():
    tipo_patologia = request.args.get("tipo_patologia")
    tipo_imagen = request.args.get("tipo_imagen")
    query = ObtenerImagenes(tipo_patologia=tipo_patologia, tipo_imagen=tipo_imagen)
    resultado = ejecutar_query(query)
    return jsonify([imagen.to_dict() for imagen in resultado.resultado]), 200