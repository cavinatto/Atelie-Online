from app import create_app
from atelie_online.models import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("Tabelas criadas.")
