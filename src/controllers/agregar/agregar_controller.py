from flask import flash
from models.agregar.ciudad import Ciudad
from models.agregar.provincia import Provincia
from models.agregar.conexiones import Conexiones

# Controladores para manejar las operaciones de agregar provincias, ciudades y rutas
# Este controlador maneja la lógica para agregar nuevas provincias, ciudades y rutas entre ellas
def agregar_provincia_controller(nombre):
    if Provincia.exists(nombre):
        flash(f"La provincia '{nombre}' ya existe.", "danger")
        return False

    nueva_provincia = Provincia.create_provincia(nombre)
    flash(f"Provincia '{nueva_provincia.nombre}' agregada correctamente.", "success")
    return True

# Controlador para agregar una ciudad
# Este controlador maneja la lógica para agregar una nueva ciudad a una provincia específica
def agregar_ciudad_controller(nombre, provincia_id, costera=False):
    if Ciudad.exists(nombre, provincia_id):
        flash(f"La ciudad '{nombre}' ya existe en la provincia seleccionada.", "danger")
        return False

    nueva_ciudad = Ciudad.create_ciudad(nombre, provincia_id, costera)
    flash(f"Ciudad '{nueva_ciudad.nombre}' agregada correctamente.", "success")
    return True

# Controlador para agregar una ruta entre dos ciudades
# Este controlador maneja la lógica para agregar una nueva conexión entre dos ciudades
# Verifica que el origen y destino sean diferentes y que la distancia sea un número válido
def agregar_ruta_controller(origen, destino, distancia):
    if origen == destino:
        flash("Origen y destino deben ser diferentes.", "danger")
        return False
    
    try:
        distancia = float(distancia)
    except ValueError:
        flash("La distancia debe ser un número válido.", "danger")
        return False

    Conexiones.create_conexion(origen, destino, distancia)
    origen_obj = Ciudad.query.get(origen)
    destino_obj = Ciudad.query.get(destino)
    flash(f"Ruta de '{origen_obj.nombre}' a '{destino_obj.nombre}' agregada correctamente con distancia {distancia}.", "success")
    return True