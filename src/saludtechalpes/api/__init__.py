import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger

app = None
# Identifica el directorio base
basedir = os.path.abspath(os.path.dirname(__file__))

DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def comenzar_consumidor():
    import threading
    import saludtechalpes.modulos.imagenes.infraestructura.consumidores as imagenes

    threading.Thread(target= imagenes.suscribirse_a_comandos).start()
    threading.Thread(target= imagenes.suscribirse_a_comandos_rollback).start()

def importar_modelos_alchemy():
    import saludtechalpes.modulos.imagenes.infraestructura.dto

def create_app(configuracion=None):
    global app
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)

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
        comenzar_consumidor()

     # Importa Blueprints
    from . import imagenes

    # Registro de Blueprints
    app.register_blueprint(imagenes.bp)
    
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
