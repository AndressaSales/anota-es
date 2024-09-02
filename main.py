from flask import Flask
from routes.notas import notas_routes
from routes.home import home_routes

app = Flask(__name__)

app.register_blueprint(home_routes)
app.register_blueprint(notas_routes , url_prefix='/notas')

if __name__ == ('__main__'):
    app.run(debug=True)