from extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Modelo de Usuario
# Este modelo representa a los usuarios en la base de datos
class User(db.Model, UserMixin):
    # Nombre de la tabla en la base de datos
    __tablename__ = 'users'
    
    # Definición de las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    admin = db.Column(db.Boolean, default=False)  
    
    # Método para crear un nuevo usuario
    # Este método recibe el nombre de usuario, email y contraseña,
    # y crea un nuevo registro en la base de datos
    @classmethod
    def create_user(cls, username, email, password):
        hashed_password = generate_password_hash(password)
        new_user = cls(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return new_user
    
    # Método para verificar si un usuario ya existe
    # Este método comprueba si ya existe un usuario con el mismo nombre de usuario o email
    @classmethod
    def exists(cls, username, email):
        if cls.query.filter((cls.username == username) | (cls.email == email)).first():
            return True
        return False
    
    # Método para verificar la contraseña del usuario
    # Este método compara la contraseña proporcionada con la almacenada en la base de datos
    def check_password(self, password):
        return check_password_hash(self.password, password)