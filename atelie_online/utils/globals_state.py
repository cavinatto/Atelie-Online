admins_cache = []

def atualizar_lista_admins(db, Usuario):
    """Atualiza lista global dos funcionários"""
    global admins_cache
    admins_cache.clear()
    admins_cache.extend(Usuario.query.filter_by(is_admin=True).all())
    
#atelie_online\utils\globals_state.py