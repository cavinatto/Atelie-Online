from flask import Flask
from atelie_online.config import Config
from atelie_online.models import db
from atelie_online.controllers.servico_controller import servico_bp



def create_app():

    
    app = Flask(__name__, template_folder="atelie_online/templates")
    
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(servico_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)

#app.py
