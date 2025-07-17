from flask_login import current_user  
from functools import wraps           
from flask import redirect, url_for

# Decorador para verificar si el usuario es administrador
# Si el usuario no está autenticado o no es administrador, redirige a una página de error
def admin_required(f): #Decorador
    @wraps(f)  #Para mantener el nombre de la funcion original
    def decorated_function(*args, **kwargs):  #La funcion decorada o la funcion que se ejecuta
        if not current_user.is_authenticated or not getattr(current_user, 'admin', False): #Condicion
            return redirect(url_for('error_admins.error_admins'))
        return f(*args, **kwargs) #Retorna los agrumentos y palabras clave de la funcion original
    return decorated_function #Retorna la funcion decorada