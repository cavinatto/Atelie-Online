# controllers/service_controller.py
from models.service_model import (
    get_all_services,
    get_service_by_id,
    create_service,
    update_service,
    delete_service
)

def list_services():
    return get_all_services()

def get_service(service_id):
    return get_service_by_id(service_id)

def add_service(name, description, price):
    return create_service(name, description, price)

def edit_service(service_id, name, description, price):
    return update_service(service_id, name, description, price)

def remove_service(service_id):
    return delete_service(service_id)