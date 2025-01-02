from flask import Flask

def create_app():
    app = Flask(__name__)

    from .routes import base

    app.register_blueprint(base.base_blueprint)

    return app