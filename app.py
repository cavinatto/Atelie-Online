from flask import Flask
from atelie_online.config import Config
from atelie_online.models import db
from atelie_online.controllers.servico_controller import servico_bp
from atelie_online.controllers.cliente_controller import cliente_bp
from atelie_online.controllers.auth_controller import auth_bp
from atelie_online.controllers.main_controller import main_bp
#Biblioteca para pegar time.sleep() - "delay"
import time
#OparationlError = tratar erros de exceção
from sqlalchemy.exc import OperationalError


def create_app():

    
    app = Flask(__name__, 
                template_folder="atelie_online/templates",
                static_folder="atelie_online/static")
    
    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(servico_bp)
    app.register_blueprint(cliente_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)

    #app_context() -> contexto de aplicação/application context, bloco do app flask ativo, permmite acesso às variáveis e seus resucros
    with app.app_context():
        
        #Quantidade de vezes que pode tentar criar ou conectar a um tabela (máximod de tentativas)
        tries_bd_conc = 5
        
        #contador que inicia no valor 1 e segue até o valor da variável tries_bd_conc (5), irá incremetar 1 a cada tentativa
        for tentar in range(1,tries_bd_conc +1):
            try:
                #Lê o SQLALCHEMY_DATABASE_URI
                db.create_all()
                break
            except OperationalError as e:
                
                #se o valor de tentativas forem exatemete iguais ao valor de contagem, ensagem de erro
                if tentar == tries_bd_conc:
                    raise RuntimeError(f"Falha ao conectar com Banco de dados após {tries_bd_conc} tentativas: {e}")
                
                #a cada 1 seegundo, uma nova tentativa de criação
                time.sleep(1)
                
                

    return app

if __name__ == '__main__':
    #comando para criar todas tabelas definidas no model
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)

#app.py
