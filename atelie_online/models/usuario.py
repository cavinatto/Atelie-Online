from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #criptografar senha para comparar coms egurança
    #entrar e atualizar planilha no postgre (ver file comandos_postgres.md)
    senha_hash = db.Column(db.String(128), nullable=False)
    
    is_admin = db.Column(db.Boolean, default=False) # True = é admin 

    data_criacao = db.Column(db.DateTime, server_default=db.func.now())

    
    def set_senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)

    def __repr__(self):
        return f"<Usuario {self.nome}>"
    
#atelie_online\models\usuario.py

