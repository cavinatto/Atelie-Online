from functools import wraps
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from atelie_online.models.cliente_model import Cliente
from atelie_online.models import db

cliente_bp = Blueprint('clientes', __name__, template_folder='../templates')

@cliente_bp.route('/')
def index():
    return redirect(url_for('clientes.cadastrar_cliente'))

@cliente_bp.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_cliente():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        telefone = request.form.get('telefone')
        cpf_cnpj = request.form.get('cpf_cnpj')
        endereco = request.form.get('endereco')

        novo_cliente = Cliente(nome, email, telefone, cpf_cnpj, endereco)
        try:
            db.session.add(novo_cliente)
            db.session.commit()
            flash('Cliente cadastrado com sucesso!', 'success')
            return redirect(url_for('clientes.listar_clientes'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao cadastrar cliente: {str(e)}', 'danger')
            return redirect(url_for('clientes.cadastrar_cliente'))

    return render_template('cadastro_cliente.html')

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'usuario_id' not in session:
            flash('Você precisa estar logado para acessar essa página.', 'danger')
            return redirect(url_for('auth.login'))
        return func(*args, **kwargs)
    return wrapper

@cliente_bp.route('/clientes')
@login_required
def listar_clientes():
    clientes = Cliente.query.all()
    return render_template('listar_clientes.html', clientes=clientes)

@cliente_bp.route('/excluir/<int:id>', methods=['POST'])
@login_required
def excluir_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    try:
        db.session.delete(cliente)
        db.session.commit()
        flash('Cliente excluído com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao excluir cliente: {str(e)}', 'danger')
    return redirect(url_for('clientes.listar_clientes'))
