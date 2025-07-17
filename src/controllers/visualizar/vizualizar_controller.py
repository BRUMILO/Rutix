from models.agregar.provincia import Provincia
from models.agregar.ciudad import Ciudad
from models.agregar.conexiones import Conexiones

def obtener_provincias_controller():
    provincias = Provincia.obtener_provincias()
    return {'provincias': provincias}

def obtener_ciudades_controller():
    ciudades = Ciudad.obtener_ciudades()
    return {'ciudades': ciudades}

def obtener_conexiones_controller():
    conexiones = Conexiones.obtener_conexiones()
    return conexiones