import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_swagger import swagger
import os

app = None
basedir = os.path.abspath(os.path.dirname(__file__))


DB_NAME = os.environ.get('DB_NAME')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get('DB_PORT')
DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')

def importar_modelos_alchemy():
    import exportacionsta.modulos.exportacion.infraestructura.dto

def create_app(configuracion=None):
    global app
    # Init la aplicacion de Flask
    app = Flask(__name__, instance_relative_config=True)
    app.config['SQLALCHEMY_DATABASE_URI'] =(
            f'postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

     # Inicializa la DB
    from exportacionsta.config.db import init_db
    init_db(app)

    from exportacionsta.config.db import db
    importar_modelos_alchemy()

    with app.app_context():
        db.create_all()

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
