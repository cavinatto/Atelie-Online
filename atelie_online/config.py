import os
from sqlalchemy import create_engine

# Configurações do banco de dados MySQL
class Config:
    # Mostra qual database da api o sqlalchemy deve importar, neste caso será bd postgres e psycop2
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","postgresql+psycopg2://atelie_user:atelie_pass@localhost:5432/atelie")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'chave-secreta'
    
def get_engine():
    return create_engine(Config.SQLALCHEMY_DATABASE_URI)
#atelie_online/config.py

