from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from atelie_online.models.usuario import Usuario
from atelie_online.models import db

auth_bp = Blueprint('auth', __name__, template_folder='../templates/auth')

# Rota para exibir formulário de registro
@auth_bp.route('/register', methods=['GET'])
def register_form():
    return render_template('registro.html')

# Rota para cadastrar novo usuário
@auth_bp.route('/register', methods=['POST'])
def register():
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']

    # Verifica se email já existe
    if Usuario.query.filter_by(email=email).first():
        flash('E-mail já cadastrado!', 'danger')
        return redirect(url_for('auth.register_form'))

    novo_usuario = Usuario(nome=nome, email=email)
    novo_usuario.set_senha(senha)

    db.session.add(novo_usuario)
    db.session.commit()

    flash('Cadastro realizado com sucesso! Faça login.', 'success')
    return redirect(url_for('auth.login_form'))

# Rota para exibir formulário de login
@auth_bp.route('/login', methods=['GET'])
def login_form():
    return render_template('login.html')

# Rota para processar login
@auth_bp.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    senha = request.form['senha']

    usuario = Usuario.query.filter_by(email=email).first()

    if usuario and usuario.verificar_senha(senha):
        session['usuario_id'] = usuario.id
        session['usuario_nome'] = usuario.nome
        flash('Login realizado com sucesso!', 'success')
        return redirect(url_for('cliente.listar_clientes'))

    flash('E-mail ou senha incorretos.', 'danger')
    return redirect(url_for('auth.login_form'))

# Rota para logout
@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logout realizado com sucesso!', 'info')
    return redirect(url_for('auth.login_form'))