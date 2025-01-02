from flask import Blueprint

base_blueprint = Blueprint('/', __name__)

@base_blueprint.route('/')
def index():
    return "index.html"