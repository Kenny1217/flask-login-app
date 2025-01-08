from flask import Blueprint, request, render_template
import bcrypt

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/register')
def register():
    return render_template('auth/register.html')

@auth_blueprint.route('/login', methods=['GET', 'POST'])
def login():

    # Check if it was a POST request
    if request.method == 'POST':

        # Store values from page
        username = request.form['username']
        unhashed_password = request.form['password']

        # Validation checks

        # Hash the password that was entered
        salt = bcrypt.gensalt()
        unhashed_password = unhashed_password.encode("utf-8")
        hashed_password = bcrypt.hashpw(unhashed_password, salt)

        # Get hashed password stored in database
        db_hashed_password = ""

        # Check if password matches the one stored in database
        passwords_match = bcrypt.checkpw(db_hashed_password, hashed_password) 

        return passwords_match

    return render_template('auth/login.html')

@auth_blueprint.route('/logout')
def logout():
    return render_template('auth/logout.html.html')

@auth_blueprint.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():

    # Check if it was a POST request
    if request.method == 'POST':

        email = request.form['email']

        # Validation checks
        
        return f"Email sent to {email}"
    
    return render_template('auth/forgot_password.html')