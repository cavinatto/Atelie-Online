import os
from flask import Flask
from atelie_online.models import db
from atelie_online.controllers.auth_controller import auth_bp
from atelie_online.controllers.cliente_controller import cliente_bp
from atelie_online.controllers.servico_controller import servico_bp

def create_app():
    app = Flask(__name__, template_folder='atelie_online/templates', static_folder='atelie_online/static')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@db:5432/atelie_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.environ.get('SECRET_KEY', 'troque_essa_chave')

    db.init_app(app)

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(servico_bp, url_prefix='/servicos')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0')
