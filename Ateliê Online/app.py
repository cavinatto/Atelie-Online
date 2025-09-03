from flask import Flask
from flask_mysqldb import MySQL
from config import Config # Importa a classe Config do arquivo config.py
# Blueprints
from routes.service_routes import service_bp
app = Flask(__name__)
app.config.from_object(Config) # Carrega as configurações da classe Config
# Conexão MySQL
mysql = MySQL(app)
# Registrando Blueprints
app.register_blueprint(service_bp, url_prefix='/services')
@app.route('/')
def home():
    return "Bem-vindo ao Ateliê Online!"
if __name__ == '__main__':
    app.run(debug=True)