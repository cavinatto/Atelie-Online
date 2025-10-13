import os
import time
import psycopg2

from app import create_app
from atelie_online.models import db

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgresql://postgres:postgres@db:5432/atelie_db')

def wait_for_db():
    print("Aguardando banco de dados...")
    while True:
        try:
            conn = psycopg2.connect(DATABASE_URL)
            conn.close()
            print("Banco disponível!")
            break
        except Exception:
            print("Banco não pronto, tentando de novo em 2s...")
            time.sleep(2)

if __name__ == '__main__':
    wait_for_db()
    app = create_app()
    with app.app_context():
        db.create_all()
        print("Tabelas criadas (se não existiam).")
    app.run(host='0.0.0.0', port=5000, debug=True)

#entrypoint.py

