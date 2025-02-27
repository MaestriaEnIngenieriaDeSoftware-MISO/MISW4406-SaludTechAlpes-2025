import saludtechalpes.seedwork.presentacion.api as api
from flask import request, jsonify
from saludtechalpes.seedwork.aplicacion.queries import ejecutar_query
from saludtechalpes.modulos.imagenes.aplicacion.queries.obtener_imagenes_medicas import ObtenerImagenes
from saludtechalpes.modulos.imagenes.aplicacion.mapeadores import MapeadorImagenDTOJson

bp = api.crear_blueprint('imagenes', '/imagenes')

@bp.route("/obtener-imagenes/<id>", methods=["GET"])
def obtener_imagenes(id = NotImplementedError):
    
    resultado = ejecutar_query(ObtenerImagenes(id))
    print(resultado)
    map_imagen = MapeadorImagenDTOJson()
    return map_imagen.dto_a_externo(resultado.resultado)