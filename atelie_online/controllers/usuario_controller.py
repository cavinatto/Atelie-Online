from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from atelie_online.models.usuario import Usuario
from atelie_online.models import db
from atelie_online.utils.globals_state import atualizar_lista_admins

usuario_bp = Blueprint('usuario', __name__, template_folder='../templates/usuario')


@usuario_bp.route('/cadastrar_usuario', methods=['GET', 'POST'])
def cadastrar_usuario():
    if not session.get('is_admin'):
        flash("Acesso negado", "danger")
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        is_admin = True if request.form.get('is_admin') == "on" else False

        if not nome or not email or not senha:
            flash("Todos os campos devem estar preenchidos", "danger")
            return redirect(url_for('usuario.cadastrar_usuario'))

        if Usuario.query.filter_by(email=email).first():
            flash("E-mail já está cadastrado", "danger")
            return redirect(url_for('usuario.cadastrar_usuario'))

        novo_usuario = Usuario(nome=nome, email=email, is_admin=is_admin)
        novo_usuario.set_senha(senha)
        db.session.add(novo_usuario)
        db.session.commit()

        atualizar_lista_admins(db, Usuario)
        flash("Usuário cadastrado com sucesso!", "success")
        return redirect(url_for('admin_dashboard'))

    return render_template('cadastrar_usuario.html')


@usuario_bp.route('/listar_admins')
def listar_admins():
    if not session.get('is_admin'):
        flash("Acesso negado", "danger")
        return redirect(url_for('auth.login'))

    from atelie_online.utils.globals_state import admins_cache
    return render_template('listar_admins.html', admins=admins_cache)

#atelie_online\controllers\usuario_controller.py

#docker compose exec web python
#abre com acesso do flask e bd