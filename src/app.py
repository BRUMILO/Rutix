# Importa la clase Flask para crear la aplicación web
from flask import Flask
# Importa las extensiones necesarias para la aplicación
from extensions import lm
# Importa la función para registrar los blueprints de rutas
from routes import register_blueprints
# Importa la configuración de la aplicación desde un archivo separado
from config import Config
# Importa la instancia de la base de datos desde extensions.py
from extensions import db
# Importa el modelo de usuario para manejar la autenticación
from models.users.User import User

def create_app():
    # Crea una instancia de la aplicación Flask
    app = Flask(__name__)
    
    # Carga la configuración de la aplicación desde la clase Config
    app.config.from_object(Config)
    
    # Inicializa la extensión de SQLAlchemy con la app
    db.init_app(app)
    
    # Inicializa Flask-Login
    lm.init_app(app)
    
    # Esta ruta se usará para redirigir a los usuarios no autenticados
    lm.login_view = 'login.login'
    
    # Registra los Blueprints de rutas
    register_blueprints(app)
    
    # Devuelve la aplicación completamente configurada
    return app

# Crea un usuario administrador si no existe
def create_user_admin(app):
    with app.app_context():
        if not User.query.filter_by(username='admin').first():
            User.create_user('admin', 'admin@email.com', 'admin123')
            admin = User.query.filter_by(username='admin').first()
            admin.admin = True
            db.session.commit()

# Crea la aplicación usando la función de fábrica
app = create_app()

# Crea un usuario administrador si no existe
create_user_admin(app)

if __name__ == '__main__':    
    app.run(debug=True)