# config.py
class Config:
    # Configurações padrão do banco MySQL
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = 'Atelie123' # Altere para a sua senha do MySQL
    MYSQL_DB = 'atelie_online'
    MYSQL_CURSORCLASS = 'DictCursor' # Importante para retornar dicionários
    # Chave secreta usada pelo Flask para sessões e segurança
    SECRET_KEY = 'chave_super_secreta' # Altere para uma chave mais segura em produção