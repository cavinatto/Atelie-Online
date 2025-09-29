from . import db

class Servico(db.Model):
    __tablename__ = 'servicos'
    id = db.Column(db.Integer, primary_key=True)
    nome_cliente = db.Column(db.String(100), nullable=False)
    tipo_servico = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=False)

    def __init__(self, nome_cliente, tipo_servico, descricao):
        self.nome_cliente = nome_cliente
        self.tipo_servico = tipo_servico
        self.descricao = descricao
