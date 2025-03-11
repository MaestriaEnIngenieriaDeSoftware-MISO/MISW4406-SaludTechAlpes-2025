import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))


def comenzar_consumidor():
    import threading
    import exportacionsta.modulos.exportacion.infraestructura.consumidores as consumidores

    threading.Thread(target= consumidores.suscribirse_a_eventos_exportaciones).start()
    threading.Thread(target= imagenes.suscribirse_a_eventos_notificaciones).start()

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    #with app.app_context():
        #comenzar_consumidor()

     # Importa Blueprints
    from . import exportacion

    # Registro de Blueprints
    app.register_blueprint(exportacion.bp)
    
    @app.route("/spec")
    def spec():
        swag = swagger(app)
        swag['info']['version'] = "1.0"
        swag['info']['title'] = "My API"
        return jsonify(swag)

    @app.route("/health")
    def health():
        return {"status": "up"}

    return app
