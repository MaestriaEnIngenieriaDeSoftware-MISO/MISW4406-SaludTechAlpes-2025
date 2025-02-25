import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger
from saludtechalpes.api.imagenes import bp as imagenes_bp

# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def importar_modelos_alchemy():
    pass
    # import aeroalpes.modulos.cliente.infraestructura.dto
    # import aeroalpes.modulos.hoteles.infraestructura.dto
    # import aeroalpes.modulos.pagos.infraestructura.dto
    # import aeroalpes.modulos.precios_dinamicos.infraestructura.dto
    # import aeroalpes.modulos.vehiculos.infraestructura.dto
    # import aeroalpes.modulos.vuelos.infraestructura.dto

def create_app(configuracion=None):
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

    # Configuracion de BD
    app.config['SQLALCHEMY_DATABASE_URI'] =(
            f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     # Inicializa la DB
    from saludtechalpes.config.db import init_db
    init_db(app)

    from saludtechalpes.config.db import db

    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()

     # Importa Blueprints
    # from . import cliente
    # from . import hoteles
    # from . import pagos
    # from . import precios_dinamicos
    # from . import vehiculos
    # from . import vuelos

    # Registro de Blueprints
    # app.register_blueprint(cliente.bp)
    # app.register_blueprint(hoteles.bp)
    # app.register_blueprint(pagos.bp)
    # app.register_blueprint(precios_dinamicos.bp)
    # app.register_blueprint(vehiculos.bp)
    # app.register_blueprint(vuelos.bp)

    app.register_blueprint(imagenes_bp)
    
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
