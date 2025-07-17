from flask import redirect, url_for, flash, session
from flask_login import login_user, logout_user, login_required
from models.users.User import User

# Controlador para el registro de usuarios
# Este controlador maneja la lógica para registrar un nuevo usuario
def register_user(username, email, password):
    if User.exists(username, email):
        flash('El usuario o email ya existe.', 'danger')
        return False

    User.create_user(username, email, password)
    flash('Usuario registrado correctamente. Ahora puedes iniciar sesión.', 'success')
    return True

# Controlador para el inicio de sesión de usuarios
# Este controlador maneja la lógica para autenticar a un usuario
def login_user_controller(username, password):
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        session.permanent = True
        flash('Bienvenido, sesión iniciada.', 'success')
        return True
    else:
        flash('Usuario o contraseña incorrectos.', 'danger')
        return False

# Controlador para el cierre de sesión de usuarios
# Este controlador maneja la lógica para cerrar la sesión del usuario actual
@login_required
def logout_user_controller():
    logout_user()
    flash('Sesión cerrada correctamente.', 'success')
    return True