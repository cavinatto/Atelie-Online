from flask import Flask
from config import Config
from models import db
from controllers.servico_controller import servico_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # registrar blueprints
    app.register_blueprint(servico_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
