from flask import Blueprint, render_template, url_for, redirect, flash
from flask_login import login_required
from controllers.home import obtener_datos_dashboard

# Blueprint para las rutas de la página de inicio y el menú
# Este archivo maneja las rutas principales de la aplicación
home_bp = Blueprint('home', __name__)
# Blueprint para el menú de navegación
# Este blueprint se usa para renderizar la plantilla base del menú
menu_bp = Blueprint('menu', __name__)

# Ruta para la página de inicio
# Redirige a la página de inicio de sesión si el usuario no está autenticado
@home_bp.route('/')
def home():
    return redirect(url_for('login.login'))  

# Ruta para el dashboard
# Esta ruta requiere que el usuario esté autenticado
@home_bp.route('/dashboard')
@login_required
def dashboard():
    data = obtener_datos_dashboard()
    return render_template('dashboard.html', **data)

# Ruta para el menú
# Esta ruta renderiza la plantilla base del menú
@menu_bp.route('/menu')
def menu():
    return render_template("base.html")
