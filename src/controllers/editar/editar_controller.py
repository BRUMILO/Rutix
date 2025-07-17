from models.agregar.provincia import Provincia
from models.agregar.ciudad import Ciudad
from models.agregar.conexiones import Conexiones

# Controlador para editar provincias, ciudades y conexiones
# Este controlador maneja la lógica para editar provincias, ciudades y conexiones en la base de datos
def editar_provincia_controller(provincia_id, nuevo_nombre):
    try:
        return Provincia.editar_provincia(provincia_id, nuevo_nombre)
    except Exception:
        return False

# Controlador para editar una ciudad
# Este controlador maneja la lógica para editar una ciudad específica por su ID
def editar_ciudad_controller(ciudad_id, nuevo_nombre, nueva_provincia_id, nueva_costera):
    try:
        return Ciudad.editar_ciudad(ciudad_id, nuevo_nombre, nueva_provincia_id, nueva_costera)
    except Exception:
        return False

# Controlador para editar una conexión
# Este controlador maneja la lógica para editar una conexión específica por su ID
def editar_conexion_controller(conexion_id, nuevo_origen_id, nuevo_destino_id, nueva_distancia):
    try:
        return Conexiones.editar_conexion(conexion_id, nuevo_origen_id, nuevo_destino_id, nueva_distancia)
    except Exception:
        return False
