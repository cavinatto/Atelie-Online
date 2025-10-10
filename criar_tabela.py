from atelie_online import create_app
from atelie_online.models import db

app = create_app()

with app.app_context():
    db.create_all()
    print("Tabelas criadas com sucesso!")
    
#comandos
# docker compose up -d
# aqui entra no interpretador interativo do Python dentro do container web (Python REPL), não executou o script ainda
# docker compose exec web python
# exit() para sair

# criar_tabela.py
# depois entra

#docker ps vê o que foi criado
# ver o nome da imagem
# docker compose exec web python criar_tabela.py
#resposta Tabelas criadas com sucesso!


