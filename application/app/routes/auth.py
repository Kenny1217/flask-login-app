from flask import Blueprint, request, render_template, url_for

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/register')
def register():
    return render_template('auth/register.html')

@auth_blueprint.route('/login')
def login():
    return render_template('auth/login.html')

@auth_blueprint.route('/logout')
def logout():
    return render_template('auth/logout.html.html')

@auth_blueprint.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        return f"Email sent to {email}"
    return render_template('auth/forgot_password.html')


    