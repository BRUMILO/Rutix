from flask import Blueprint, render_template
from flask_login import login_required

# Blueprint para las rutas de advertencias
# Este archivo maneja las rutas para mostrar advertencias y errores de administrador
error_admins_bp = Blueprint('error_admins', __name__)

# Ruta para mostrar la advertencia de administrador
# Esta ruta se usa para mostrar un mensaje de error si el usuario no es administrador
@error_admins_bp.route('/error_admins')
@login_required
def error_admins():
    return render_template('advertencia/admin.html')