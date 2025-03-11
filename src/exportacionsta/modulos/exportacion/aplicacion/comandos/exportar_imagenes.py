
from exportacionsta.seedwork.aplicacion.comandos import ComandoHandler, Comando, ejecutar_commando as comando
from exportacionsta.modulos.exportacion.dominio.objetos_valor import Estado
from exportacionsta.modulos.exportacion.dominio.entidades import Operacion
from dataclasses import dataclass
from exportacionsta.modulos.exportacion.infraestructura.despachadores import Despachador
from .base import RegistrarOperacionBaseHandler
from exportacionsta.modulos.exportacion.infraestructura.repositorios import RepositorioOperaciones
from exportacionsta.modulos.exportacion.aplicacion.dto import RegistrarOperacionDTO
from exportacionsta.modulos.exportacion.aplicacion.mapeadores import MapeadorOperacionesDTO

@dataclass
class ExportarImagenes(Comando):
    tipo_imagen: str
    tipo_patologia: str

@dataclass
class RegistrarOperacion(Comando):
    estado: Estado

class ExportarImagenesHandler(ComandoHandler):

    def handle(self,comando: ExportarImagenes):
        despachador = Despachador()
        despachador.publicar_comando(comando,'comandos-obtener-imagenes')

class RegistrarOperacionHadler(RegistrarOperacionBaseHandler):
    def handle(self,comando: RegistrarOperacion):
        operacionDTO = RegistrarOperacionDTO(estado=Estado.INICIADO)
        operacion: Operacion = self.fabrica_operaciones.crear_objeto(operacionDTO, MapeadorOperacionesDTO())
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioOperaciones.__class__)
        repositorio.agregar(operacion)

@comando.register(ExportarImagenes)
def ejecutar_comando_exportar_imagenes(comando: ExportarImagenes):
    handler = ExportarImagenesHandler()
    handler.handle(comando)

@comando.register()
def ejecutar_comando_registrar_operacion():
    comando_registrar_operacion = RegistrarOperacion(estado = Estado.INICIADO)
    handler_operaciones = RegistrarOperacionHadler()
    handler_operaciones.handle(comando_registrar_operacion)
    