import os

# Configurações do banco de dados MySQL
class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","mysql+pymysql://root:Enzo39824360@db:3306/atelie")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'chave-secreta'

#atelie_online/config.py