from atelie_online import create_app
from atelie_online.models import db

app = create_app()

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")
