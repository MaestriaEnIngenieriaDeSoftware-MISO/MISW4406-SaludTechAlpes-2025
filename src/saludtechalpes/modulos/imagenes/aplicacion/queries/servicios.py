from saludtechalpes.seedwork.aplicacion.servicios import Servicio
from saludtechalpes.modulos.imagenes.infraestructura.fabricas import FabricaRepositorio
from saludtechalpes.modulos.imagenes.aplicacion.dto import ObtenerImagenesDTO, ImagenesDTO
from saludtechalpes.modulos.imagenes.infraestructura.repositorios import RepositorioImagenes
from saludtechalpes.modulos.imagenes.dominio.fabricas import FabricaImagen
from saludtechalpes.modulos.imagenes.infraestructura.repositorios import MapeadorImagenes

class ServicioImagenes(Servicio):

    def __init__(self):
        self._fabrica_repositorio = FabricaRepositorio()
        self._fabrica_imagen = FabricaImagen()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_imagen(self):
        return self._fabrica_imagen    
    
    def consultar_imagenes_por_query(self, query_dto: ObtenerImagenesDTO) -> ImagenesDTO:
        repositorio =  self.fabrica_repositorio.crear_objeto(RepositorioImagenes.__class__)
        return self._fabrica_imagen.crear_objeto(repositorio.consultar_entidades_por_parametros(query_dto), MapeadorImagenes())