from extensions import db

# Modelo de Conexiones
# Este modelo representa las conexiones entre ciudades en la base de datos
class Conexiones(db.Model):
    # Nombre de la tabla en la base de datos
    __tablename__ = 'conexiones'
    
    # Definición de las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)
    origen_id = db.Column(db.Integer, db.ForeignKey('ciudades.id'), nullable=False)
    destino_id = db.Column(db.Integer, db.ForeignKey('ciudades.id'), nullable=False)
    distancia = db.Column(db.Float, nullable=False)

    # Relaciones con el modelo Ciudad
    # Estas relaciones permiten acceder a las ciudades de origen y destino de una conexión
    origen = db.relationship('Ciudad', foreign_keys=[origen_id], backref='conexiones_salida')
    destino = db.relationship('Ciudad', foreign_keys=[destino_id], backref='conexiones_entrada')
    
    # Métodos de clase para manejar las operaciones CRUD
    @classmethod
    def create_conexion(cls, origen_id, destino_id, distancia):
        nueva_conexion = cls(origen_id=origen_id, destino_id=destino_id, distancia=distancia)
        db.session.add(nueva_conexion)
        db.session.commit()
        return nueva_conexion
    
    # Método para verificar si una conexión ya existe
    # Este método comprueba si ya existe una conexión entre dos ciudades
    @classmethod
    def obtener_conexiones(cls):
        conexiones = cls.query.all()
        return [(conexion.origen.nombre, conexion.destino.nombre, conexion.distancia) for conexion in conexiones]
    
    # Método para verificar si una conexión ya existe
    # Este método comprueba si ya existe una conexión entre dos ciudades específicas
    @classmethod
    def eliminar_conexiones_por_ciudad(cls, ciudad_id):
        try:
            conexiones = cls.query.filter((cls.origen_id == ciudad_id) | (cls.destino_id == ciudad_id)).all()
            for conexion in conexiones:
                db.session.delete(conexion)
            
            db.session.commit()
            return True
        except Exception:
            db.session.rollback()
            return False
    
    # Método para eliminar una conexión por su ID
    # Este método elimina una conexión específica por su ID
    @classmethod
    def eliminar_conexion(cls, conexion_id):
        try:
            conexion = cls.query.get(conexion_id)
            if conexion:
                db.session.delete(conexion)
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False
    
    # Método para editar una conexión
    # Este método permite modificar los detalles de una conexión específica por su ID
    @classmethod
    def editar_conexion(cls, conexion_id, nuevo_origen_id, nuevo_destino_id, nueva_distancia):
        try:
            conexion = cls.query.get(conexion_id)
            if conexion:
                conexion.origen_id = nuevo_origen_id
                conexion.destino_id = nuevo_destino_id
                conexion.distancia = nueva_distancia
                db.session.commit()
                return True
            return False
        except Exception:
            db.session.rollback()
            return False