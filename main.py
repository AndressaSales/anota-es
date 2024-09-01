from flask import Flask
from routes.notas import notas_routes
app = Flask(__name__)

app.register_blueprint(notas_routes)

if __name__ == ('__main__'):
    app.run(debug=True)