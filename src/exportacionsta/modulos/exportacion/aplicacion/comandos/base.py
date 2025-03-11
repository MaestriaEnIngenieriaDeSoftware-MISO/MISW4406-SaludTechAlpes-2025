from exportacionsta.seedwork.aplicacion.comandos import ComandoHandler
from exportacionsta.modulos.exportacion.infraestructura.fabricas import FabricaRepositorio
from exportacionsta.modulos.exportacion.dominio.fabricas import FabricaOperaciones

class RegistrarOperacionBaseHandler(ComandoHandler):
    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()
        self._fabrica_operaciones: FabricaOperaciones = FabricaOperaciones()

    @property
    def fabrica_repositorio(self):
        return self._fabrica_repositorio
    
    @property
    def fabrica_operaciones(self):
        return self._fabrica_operaciones    