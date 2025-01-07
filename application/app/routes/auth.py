from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/register')
def register():
    return "Register"

@auth_blueprint.route('/login')
def login():
    return "Login"

@auth_blueprint.route('/logout')
def logout():
    return "Logout"

@auth_blueprint.route('/forgot_password')
def forgot_password():
    return "Forgot Password"