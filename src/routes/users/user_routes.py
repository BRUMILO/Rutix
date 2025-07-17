from flask import Blueprint, render_template, request, flash, redirect, url_for
from controllers.users.users_controllers import register_user, login_user_controller, logout_user_controller

# Blueprint para las rutas de usuarios
# Este archivo maneja las rutas de inicio de sesión, registro y cierre de sesión
login_bp = Blueprint('login', __name__)
# Blueprint para el registro de usuarios
# Este blueprint se usa para registrar nuevos usuarios en la aplicación
register_bp = Blueprint('register', __name__)
# Blueprint para el cierre de sesión
# Este blueprint se usa para cerrar la sesión del usuario actual
logout_bp = Blueprint('logout', __name__)

# Ruta para iniciar sesión
# Esta ruta maneja tanto el método GET para mostrar el formulario de inicio de sesión
@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username and password:
            if login_user_controller(username, password):
                return redirect(url_for('home.dashboard'))
        
        return render_template('users/login.html')
    return render_template('users/login.html')

# Ruta para registrar un nuevo usuario
# Esta ruta maneja tanto el método GET para mostrar el formulario de registro
@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if not all([username, email, password, confirm_password]):
            flash('Todos los campos son obligatorios.', 'danger')
            return render_template('users/register.html')
        
        if password != confirm_password:
            flash('Las contraseñas no coinciden.', 'danger')
            return render_template('users/register.html')
        
        if register_user(username, email, password):
            return redirect(url_for('login.login'))
        
        return render_template('users/register.html')
    
    return render_template('users/register.html')

# Ruta para cerrar sesión
# Esta ruta maneja el cierre de sesión del usuario actual
@logout_bp.route('/logout')
def logout():
    logout_user_controller()
    return redirect(url_for('login.login'))