import os

# Configurações do banco de dados MySQL
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Enzo39824360@localhost/atelie_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'chave-secreta'
