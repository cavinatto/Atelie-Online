# models/service_model.py
from flask import current_app

def _get_cursor():
    # current_app.extensions['mysql'].connection acessa a conexão MySQL
    # configurada em app.py. O cursor será do tipo DictCursor se configurado.
    conn = current_app.extensions['mysql'].connection
    return conn.cursor()

def get_all_services():
    cur = _get_cursor()
    cur.execute("SELECT * FROM services ORDER BY id DESC")
    services = cur.fetchall() # Retorna lista de dicionários (se DictCursor)
    cur.close()
    return services

def get_service_by_id(service_id):
    cur = _get_cursor()
    cur.execute("SELECT * FROM services WHERE id = %s", (service_id,))
    service = cur.fetchone() # Retorna um dicionário (se DictCursor)
    cur.close()
    return service

def create_service(name, description, price):
    conn = current_app.extensions['mysql'].connection
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO services (name, description, price) VALUES (%s, %s, %s)",
        (name, description, price)
    )
    conn.commit() # Confirma a transação
    cur.close()
    return cur.lastrowid # Retorna o ID do serviço recém-criado

def update_service(service_id, name, description, price):
    conn = current_app.extensions['mysql'].connection
    cur = conn.cursor()
    cur.execute(
        "UPDATE services SET name=%s, description=%s, price=%s WHERE id=%s",
        (name, description, price, service_id)
    )
    conn.commit()
    cur.close()

def delete_service(service_id):
    conn = current_app.extensions['mysql'].connection
    cur = conn.cursor()
    cur.execute("DELETE FROM services WHERE id=%s", (service_id,))
    conn.commit()
    cur.close()