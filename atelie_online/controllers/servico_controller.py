from flask import Blueprint, render_template, request, redirect, url_for, flash
from atelie_online.models.servico_model import Servico
from atelie_online.models import db

servico_bp = Blueprint('servico', __name__, template_folder='../templates')

@servico_bp.route('/')
def index():
    return redirect(url_for('servico.cadastrar_servico'))

@servico_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_servico():
    if request.method == 'POST':
        nome_cliente = request.form['nome_cliente']
        tipo_servico = request.form['tipo_servico']
        descricao = request.form['descricao']

        novo_servico = Servico(nome_cliente, tipo_servico, descricao)
        db.session.add(novo_servico)
        db.session.commit()
        flash('Serviço cadastrado com sucesso!', 'success')
        return redirect(url_for('servico.listar_servicos'))

    return render_template('cadastro_servico.html')

@servico_bp.route('/servicos')
def listar_servicos():
    servicos = Servico.query.all()
    return render_template('lista_servicos.html', servicos=servicos)

@servico_bp.route('/excluir/<int:id>', methods=['POST'])
def excluir_servico(id):
    servico = Servico.query.get_or_404(id)
    db.session.delete(servico)
    db.session.commit()
    flash('Serviço excluído com sucesso!', 'success')
    return redirect(url_for('servico.listar_servicos'))
#atelie_online/controllers/servico_controller.py
