from flask import Blueprint, request, jsonify
from src.saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
from src.saludtechalpes.modulos.imagenes.aplicacion.queries.obtener_imagenes_medicas import ObtenerImagenes

bp = Blueprint('imagenes', __name__, url_prefix='/imagenes')

@bp.route("/obtener-imagenes", methods=["GET"])
def obtener_imagenes():
    tipo_patologia = request.args.get("tipo_patologia")
    tipo_imagen = request.args.get("tipo_imagen")
    query = ObtenerImagenes(tipo_patologia=tipo_patologia, tipo_imagen=tipo_imagen)
    resultado = ejecutar_query(query)
    return jsonify([imagen.to_dict() for imagen in resultado.resultado]), 200