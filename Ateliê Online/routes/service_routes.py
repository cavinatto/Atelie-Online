# routes/service_routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.service_controller import (
    list_services,
    get_service,
    add_service,
    edit_service,
    remove_service
)

# Define o Blueprint para os serviços
# template_folder aponta para a pasta 'templates' na raiz do projeto
# static_folder aponta para a pasta 'static' na raiz do projeto
service_bp = Blueprint('services', __name__, template_folder='../templates', static_folder='../static')

# Rota para listar todos os serviços
@service_bp.route('/')
def services_list():
    services = list_services()
    return render_template('services/list.html', services=services)

# Rota para criar um novo serviço (GET para exibir formulário, POST para submeter)
@service_bp.route('/create', methods=['GET', 'POST'])
def create_service():
    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        price = request.form.get('price', '0').strip()

        # Validação básica
        if not name or not price:
            flash('Nome e preço são obrigatórios.')
            return redirect(url_for('services.create_service'))

        # Tenta converter preço para float, com tratamento de erro
        try:
            price = float(price)
        except ValueError:
            flash('Preço inválido. Use um formato numérico.')
            return redirect(url_for('services.create_service'))

        add_service(name, description, price)
        flash('Serviço criado com sucesso!')
        return redirect(url_for('services.services_list'))

    return render_template('services/create.html')

# Rota para editar um serviço existente (GET para exibir formulário, POST para submeter)
@service_bp.route('/edit/<int:service_id>', methods=['GET', 'POST'])
def edit_service_route(service_id):
    service = get_service(service_id)
    if not service:
        flash('Serviço não encontrado.')
        return redirect(url_for('services.services_list'))

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        description = request.form.get('description', '').strip()
        price = request.form.get('price', '0').strip()

        # Validação básica
        if not name or not price:
            flash('Nome e preço são obrigatórios.')
            return redirect(url_for('services.edit_service_route', service_id=service_id))

        # Tenta converter preço para float, com tratamento de erro
        try:
            price = float(price)
        except ValueError:
            flash('Preço inválido. Use um formato numérico.')
            return redirect(url_for('services.edit_service_route', service_id=service_id))

        edit_service(service_id, name, description, price)
        flash('Serviço atualizado com sucesso!')
        return redirect(url_for('services.services_list'))

    return render_template('services/edit.html', service=service)

# Rota para excluir um serviço (apenas POST)
@service_bp.route('/delete/<int:service_id>', methods=['POST'])
def delete_service_route(service_id):
    remove_service(service_id)
    flash('Serviço excluído com sucesso!')
    return redirect(url_for('services.services_list'))