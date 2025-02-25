from flask import Blueprint, request, jsonify
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
#from saludtechalpes.modulos.imagenes.aplicacion.queries.obtener_imagenes_medicas import ObtenerImagenes
from saludtechalpes.modulos.imagenes.aplicacion.queries.servicios import ServicioImagenes
from saludtechalpes.modulos.imagenes.aplicacion.dto import ObtenerImagenesDTO

bp = Blueprint('imagenes', __name__, url_prefix='/imagenes')

@bp.route("/obtener-imagenes", methods=["GET"])
def obtener_imagenes():
    tipo_patologia = request.args.get("tipo_patologia")
    tipo_imagen = request.args.get("tipo_imagen")
    query = ObtenerImagenesDTO(tipo_patologia=tipo_patologia, tipo_imagen=tipo_imagen)
    servicio = ServicioImagenes()
    imagenes = servicio.consultar_imagenes_por_query(query)
    return jsonify([imagen.to_dict() for imagen in imagenes]), 200