from atelie_online.models.usuario import Usuario

def get_adim(db):
    return Usuario.query.filter_by(is_admin=True).all()

def get_list_adim(db):
    admins = get_adim(db)
    print("Funcionários:")
    for adm in admins:
        print(f"{adm.id} | {adm.nome} | {Ad}")

#atelie_online\utils\list_admin.py