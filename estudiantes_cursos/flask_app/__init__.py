from flask import Flask

from flask_app.controllers.cursos import cursos_bp
from flask_app.controllers.estudiantes import estudiantes_bp


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "clave-local-cambiar-despues"

    app.register_blueprint(cursos_bp)
    app.register_blueprint(estudiantes_bp)

    return app
