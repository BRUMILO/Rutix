from models.agregar.provincia import Provincia
from models.agregar.ciudad import Ciudad
from models.agregar.conexiones import Conexiones

# Controlador para eliminar provincias, ciudades y conexiones
# Este controlador maneja la lógica para eliminar provincias, ciudades y conexiones de la base de datos
def eliminar_provincia_controller(provincia_id):
    try:
        return Provincia.eliminar_provincia(provincia_id)
    except Exception:
        return False

# Controlador para eliminar una ciudad
# Este controlador maneja la lógica para eliminar una ciudad específica por su ID
def eliminar_ciudad_controller(ciudad_id):
    try:
        return Ciudad.eliminar_ciudad(ciudad_id)
    except Exception:
        return False

# Controlador para eliminar una conexión
# Este controlador maneja la lógica para eliminar una conexión específica por su ID
def eliminar_conexion_controller(conexion_id):
    try:
        return Conexiones.eliminar_conexion(conexion_id)
    except Exception:
        return False