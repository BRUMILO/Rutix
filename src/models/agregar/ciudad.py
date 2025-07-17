from extensions import db
from .conexiones import Conexiones

# Modelo de Ciudad
# Este modelo representa las ciudades en la base de datos
class Ciudad(db.Model):
    # Nombre de la tabla en la base de datos
    __tablename__ = 'ciudades'
    
    # Definición de las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    provincia_id = db.Column(db.Integer, db.ForeignKey('provincias.id'), nullable=False)
    provincia = db.relationship('Provincia', backref='ciudades')
    costera = db.Column(db.Boolean, default=False)
    
    # Métodos de clase para manejar las operaciones CRUD
    @classmethod
    def create_ciudad(cls, nombre, provincia_id, costera=False):
        nueva_ciudad = cls(nombre=nombre, provincia_id=provincia_id, costera=costera)
        db.session.add(nueva_ciudad)
        db.session.commit()
        return nueva_ciudad
    
    # Método para verificar si una ciudad ya existe
    # Este método comprueba si ya existe una ciudad con el mismo nombre en la misma provincia
    @classmethod
    def exists(cls, nombre, provincia_id):
        if cls.query.filter_by(nombre=nombre, provincia_id=provincia_id).first():
            return True
        return False
    
    # Método para obtener una lista de ciudades costeras
    # Este método devuelve un conjunto de nombres de ciudades que son costeras
    @classmethod
    def obtener_ciudades_costeras(cls):
        ciudades_costeras = []
        for ciudad in cls.query.filter_by(costera=True).all():
            ciudades_costeras.append(ciudad.nombre)
        return set(ciudades_costeras)
    
    # Método para obtener todas las ciudades
    # Este método devuelve una lista de diccionarios con los datos de todas las ciudades
    @classmethod
    def obtener_ciudades(cls):
        ciudades = cls.query.all()
        return [{'id' : ciudad.id, 'nombre' : ciudad.nombre, 'provincia' : ciudad.provincia.nombre, 'provincia_id': ciudad.provincia_id, 'costera' : ciudad.costera} for ciudad in ciudades]
    
    # Métodos para editar y eliminar ciudades
    # Estos métodos permiten modificar o eliminar una ciudad específica por su ID
    @classmethod
    def editar_ciudad(cls, ciudad_id, nuevo_nombre, nueva_provincia_id, nueva_costera):
        try:
            ciudad = cls.query.get(ciudad_id)
            if ciudad:
                ciudad.nombre = nuevo_nombre
                ciudad.provincia_id = nueva_provincia_id
                ciudad.costera = nueva_costera
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False
    
    # Método para eliminar una ciudad por su ID
    # Este método elimina una ciudad y sus conexiones asociadas
    @classmethod
    def eliminar_ciudad(cls, ciudad_id):
        try:
            ciudad = cls.query.get(ciudad_id)
            if ciudad:                
                Conexiones.eliminar_conexiones_por_ciudad(ciudad_id)
                db.session.delete(ciudad)
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False
    
    # Método para eliminar todas las ciudades de una provincia
    # Este método elimina todas las ciudades asociadas a una provincia específica
    @classmethod
    def eliminar_ciudades_por_provincia(cls, provincia_id):
        try:
            ciudades = cls.query.filter_by(provincia_id=provincia_id).all()
            for ciudad in ciudades:
                cls.eliminar_ciudad(ciudad.id)

            return True
        except Exception:
            db.session.rollback()
            return False
