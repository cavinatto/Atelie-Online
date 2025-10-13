from flask import Blueprint, render_template, request, redirect, url_for, flash
from atelie_online.models.servico_model import Servico
from atelie_online.models import db

servico_bp = Blueprint('servicos', __name__, template_folder='../templates')

@servico_bp.route('/')
def index():
    return redirect(url_for('servicos.cadastrar_servico'))

@servico_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_servico():
    if request.method == 'POST':
        nome_cliente = request.form.get('nome_cliente')
        tipo_servico = request.form.get('tipo_servico')
        descricao = request.form.get('descricao')

        novo_servico = Servico(nome_cliente, tipo_servico, descricao)
        try:
            db.session.add(novo_servico)
            db.session.commit()
            flash('Serviço cadastrado com sucesso!', 'success')
            return redirect(url_for('servicos.listar_servicos'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao cadastrar serviço: {str(e)}', 'danger')
            return redirect(url_for('servicos.cadastrar_servico'))

    return render_template('cadastro_servico.html')

@servico_bp.route('/servicos')
def listar_servicos():
    servicos = Servico.query.all()
    return render_template('lista_servicos.html', servicos=servicos)

@servico_bp.route('/excluir/<int:id>', methods=['POST'])
def excluir_servico(id):
    servico = Servico.query.get_or_404(id)
    try:
        db.session.delete(servico)
        db.session.commit()
        flash('Serviço excluído com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao excluir serviço: {str(e)}', 'danger')
    return redirect(url_for('servicos.listar_servicos'))

#arrumar rota ainda
@servico_bp.route('/projeto')
def projeto():
    return render_template('projeto.html')

@servico_bp.route('/estamparia')
def estamparia():
    return render_template('estamparia.html')

@servico_bp.route('/conserto')
def conserto():
    return render_template('conserto.html')

@servico_bp.route('/customizacao')
def customizacao():
    return render_template('customizacao.html')

@servico_bp.route('/material')
def material():
    return render_template('mat_cons.html')

#atelie_online\controllers\servico_controller.py

