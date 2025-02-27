from exportacionsta.seedwork.aplicacion.servicios import Servicio


class ServicioExportacion(Servicio):

    def __init__(self):
        self._fabrica_repositorio: FabricaRepositorio = FabricaRepositorio()