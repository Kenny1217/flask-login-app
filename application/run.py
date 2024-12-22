from app import create_app

app = create_app()

if __name__ == '__name__':
    app.run(debug=True, host='0.0.0.0', port='8080')
