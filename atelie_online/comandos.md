### instalar libs como flask-migrate que é para bd, e deixa web pronta

docker compose build --no-cache

docker compose up -d

### rotar container web

docker compose exec web bash

### entrar container web flask

docker compose exec web bash

#### iniciar Flask-migrates

flask db init

#### criar tabelas

flask db migrate

resposta:

INFO  [alembic.autogenerate.compare] Detected added table 'clientes'
INFO  [alembic.autogenerate.compare] Detected added table 'servicos'
INFO  [alembic.autogenerate.compare] Detected added table 'usuarios'

tem as 3 tabelas que criei no postgres

#### apdate no bd

flask db upgrade

docker compose exec web python
from atelie_online import create_app
from atelie_online.models import db
from atelie_online.models.usuario import Usuario
app = create_app()
with app.app_context():
    admin = Usuario(nome="CEO", email="sakonon570@arqsis.com", is_admin=True)
    admin.set_senha("123temp")
    db.session.add(admin)
    db.session.commit()
    print("Admin criado com sucesso!")