from . import db

class Cliente(db.Model):
    __tablename__ = 'clientes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    telefone = db.Column(db.String(15))
    cpf_cnpj = db.Column(db.String(20))
    endereco = db.Column(db.String(255))

    def __init__(self, nome, email, telefone=None, cpf_cnpj=None, endereco=None):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.cpf_cnpj = cpf_cnpj
        self.endereco = endereco

#atelie_online\models\cliente_model.py

