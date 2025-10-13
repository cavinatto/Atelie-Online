# torna o pacote reconhecível
import os
from flask import Flask
from atelie_online.models import db
from atelie_online.controllers.auth_controller import auth_bp
from atelie_online.controllers.cliente_controller import cliente_bp
from atelie_online.controllers.servico_controller import servico_bp

def create_app():
    app = Flask(
        __name__,
        template_folder='atelie_online/templates',
        static_folder='atelie_online/static'
    )

    # Configurações do banco
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@db:5432/atelie_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = os.environ.get('SECRET_KEY', 'troque_essa_chave')

    # Inicializa o SQLAlchemy
    db.init_app(app)

    # Registra Blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(cliente_bp, url_prefix='/clientes')
    app.register_blueprint(servico_bp, url_prefix='/servicos')

    return app

#atelie_online\__init__.py

