from extensions import db
from .ciudad import Ciudad

# Modelo de Provincia
# Este modelo representa las provincias en la base de datos
class Provincia(db.Model):
    # Nombre de la tabla en la base de datos
    __tablename__ = 'provincias'
    
    # Definición de las columnas de la tabla
    # Cada provincia tiene un ID único y un nombre
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False, unique=True)
    
    # Métodos de clase para manejar las operaciones CRUD
    # Estos métodos permiten crear, editar, eliminar y consultar provincias en la base de datos
    @classmethod
    def create_provincia(cls, nombre):
        nueva_provincia = cls(nombre=nombre)
        db.session.add(nueva_provincia)
        db.session.commit()
        return nueva_provincia
    
    # Método para verificar si una provincia ya existe
    # Este método comprueba si ya existe una provincia con el mismo nombre
    @classmethod
    def exists(cls, nombre):
        if cls.query.filter_by(nombre=nombre).first():
            return True
        return False
    
    # Método para obtener todas las provincias
    # Este método devuelve una lista de diccionarios con los datos de todas las provincias
    @classmethod
    def obtener_provincias(cls):
        provincias = cls.query.all()
        return [{'id': provincia.id, 'nombre': provincia.nombre} for provincia in provincias]
    
    # Métodos para editar y eliminar provincias
    # Estos métodos permiten modificar o eliminar una provincia específica por su ID
    @classmethod
    def editar_provincia(cls, provincia_id, nuevo_nombre):
        try:
            provincia = cls.query.get(provincia_id)
            if provincia:
                provincia.nombre = nuevo_nombre
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False
    
    # Método para eliminar una provincia por su ID
    # Este método elimina una provincia específica por su ID y también elimina las ciudades asociadas
    @classmethod
    def eliminar_provincia(cls, provincia_id):
        try:
            provincia = cls.query.get(provincia_id)
            if provincia:                
                Ciudad.eliminar_ciudades_por_provincia(provincia_id)
                db.session.delete(provincia)
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False