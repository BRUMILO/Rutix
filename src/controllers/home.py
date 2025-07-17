from flask_login import current_user
from models.agregar.provincia import Provincia
from models.agregar.ciudad import Ciudad
from models.agregar.conexiones import Conexiones

# Controlador para el dashboard
# Este controlador maneja la lógica para obtener los datos necesarios para el dashboard
def obtener_datos_dashboard():
    # Obtener estadísticas del sistema
    total_provincias = Provincia.query.count()
    total_ciudades = Ciudad.query.count()
    total_rutas = Conexiones.query.count()
    
    # Información del usuario actual
    usuario = current_user
    
    # Retornar los datos para el dashboard
    # Estos datos incluyen el total de provincias, ciudades, rutas y la información del usuario
    return {
        'total_provincias': total_provincias,
        'total_ciudades': total_ciudades,
        'total_rutas': total_rutas,
        'usuario': usuario
    }