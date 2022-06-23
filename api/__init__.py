from flask import Flask
from firebase_admin import credentials,initialize_app
from sympy import I

cred = credentials.Certificate("api/key.json")
default_app = initialize_app(cred)

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'camilo201248'

    from .datosAPI import datosAPI

    app.register_blueprint(datosAPI, url_prefix='/datos')

    return app
