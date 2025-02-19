from flask import Blueprint, request, render_template
import bcrypt
from app.utilities.utilities import string_contains_whitespaces_or_empty, stings_match, string_match_length

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

@auth_blueprint.route('/register',  methods=['GET', 'POST'])
def register():

    # Check if it was a POST request
    if request.method == 'POST':

        # Store values from page
        username = request.form['username']
        email = request.form['email']
        unhashed_password = request.form['password']
        unhashed_password2 = request.form['password2']

        PASSWORD_MIN_LEN = 8
        # Validation checks
        if stings_match(unhashed_password, unhashed_password2):
            return render_template('auth/register.html')
        
        if string_contains_whitespaces_or_empty(username) or string_contains_whitespaces_or_empty(email) or \
            string_contains_whitespaces_or_empty(unhashed_password) or string_contains_whitespaces_or_empty(unhashed_password2):
            return render_template('auth/register.html')
        
        if string_match_length(unhashed_password, PASSWORD_MIN_LEN):
            return render_template('auth/register.html')
        
        # Hash the password that was entered
        salt = bcrypt.gensalt()
        unhashed_password = unhashed_password.encode("utf-8")
        hashed_password = bcrypt.hashpw(unhashed_password, salt)

        # Create user in database

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