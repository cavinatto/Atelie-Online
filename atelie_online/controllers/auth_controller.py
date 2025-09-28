from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from atelie_online.models.usuario import Usuario
from atelie_online.models import db

# Criando o Blueprint para autenticação
auth_bp = Blueprint('auth', __name__, template_folder='../templates/auth')

# =========================
# Rota de Registro
# =========================
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')

        # Validações básicas
        if not nome or not email or not senha:
            flash('Todos os campos são obrigatórios!', 'danger')
            return redirect(url_for('auth.register'))

        # Verifica se e-mail já está cadastrado
        if Usuario.query.filter_by(email=email).first():
            flash('E-mail já cadastrado!', 'danger')
            return redirect(url_for('auth.register'))

        # Cria o novo usuário
        novo_usuario = Usuario(nome=nome, email=email)
        novo_usuario.set_senha(senha)  # garante que está sendo salvo com hash

        try:
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Cadastro realizado com sucesso! Faça login.', 'success')
            return redirect(url_for('auth.login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Ocorreu um erro ao cadastrar: {str(e)}', 'danger')
            return redirect(url_for('auth.register'))

    return render_template('registro.html')


# =========================
# Rota de Login
# =========================
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.verificar_senha(senha):
            # Armazena informações na sessão
            session['usuario_id'] = usuario.id
            session['usuario_nome'] = usuario.nome

            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('cliente.listar_clientes'))

        flash('E-mail ou senha incorretos.', 'danger')
        return redirect(url_for('auth.login'))

    return render_template('login.html')


# =========================
# Rota de Logout
# =========================
@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logout realizado com sucesso!', 'info')
    return redirect(url_for('auth.login'))
