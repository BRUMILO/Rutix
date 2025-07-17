# Importa la clase SQLAlchemy, que permite usar un ORM (Object Relational Mapper)
# para interactuar con la base de datos en Flask de forma orientada a objetos
from flask_sqlalchemy import SQLAlchemy
# Crea una instancia global de SQLAlchemy llamada 'db'
# Esta instancia será compartida por todos los modelos y controladores que necesiten acceso a la base de datos
db = SQLAlchemy()

# Importa la clase LoginManager, que maneja la autenticación de usuarios en Flask
# Permite gestionar sesiones de usuario, iniciar sesión, cerrar sesión, etc.
from flask_login import LoginManager
# Importa el modelo User, que representa a los usuarios en la base de datos
# Este modelo define la estructura de los datos de usuario y contiene métodos para autenticación
from models.users.User import User

# Crea una instancia global de LoginManager llamada 'lm'
# Esta instancia se encargará de gestionar la autenticación de usuarios en la aplicación Flask
lm = LoginManager()

# Configura el LoginManager para redirigir a los usuarios no autenticados a la página de inicio de sesión
@lm.user_loader
# Esta función se usa para cargar un usuario dado su ID
# Flask-Login llamará a esta función cada vez que necesite cargar un usuario autenticado
def load_user(user_id):
    return User.query.get(int(user_id))