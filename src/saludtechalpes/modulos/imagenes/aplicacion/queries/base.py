from saludtechalpes.seedwork.aplicacion.queries import QueryHandler
from saludtechalpes.modulos.imagenes.infraestructura.fabricas import FabricaRepositorio
class ImagenesQueryBaseHandler(QueryHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
    
    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
