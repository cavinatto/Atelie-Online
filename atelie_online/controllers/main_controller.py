from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__, template_folder='../templates')

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/projeto')
def projeto():
    return render_template('projeto.html')

@main_bp.route('/estamparia')
def estamparia():
    return "<h1>Página Estamparia - Em construção</h1>"

@main_bp.route('/conserto')
def conserto():
    return "<h1>Página Conserto - Em construção</h1>"

@main_bp.route('/customizacao')
def customizacao():
    return "<h1>Página Customização - Em construção</h1>"
