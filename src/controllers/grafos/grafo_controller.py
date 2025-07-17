from flask import url_for
from models.agregar.ciudad import Ciudad
from models.agregar.conexiones import Conexiones
from utils.grafos.grafo_utils import construir_grafo, camino_optimo_con_costera, grafo_a_imagen, grafo_a_imagen_marcado

# Controlador para manejar las operaciones relacionadas con los grafos
# Este controlador maneja la lógica para construir grafos, calcular caminos óptimos y generar imágenes de los grafos
def obtener_camino_formulario_get():
    ciudades = Ciudad.obtener_ciudades()
    ciudades_nombre = [ciudad['nombre'] for ciudad in ciudades]
    imagen = 'img/grafo.png'
    return {
        'ciudades': ciudades_nombre,
        'resultado': None,
        'imagen': imagen
    }

# Controlador para manejar el formulario de búsqueda de caminos
# Este controlador maneja la lógica para obtener el camino óptimo entre dos ciudades
def obtener_camino_formulario_post(origen, destino):
    try:
        ciudades = Ciudad.obtener_ciudades()
        ciudades_nombre = [ciudad['nombre'] for ciudad in ciudades]
        aristas = Conexiones.obtener_conexiones()
        resultado = None
        imagen = 'img/grafo.png'

        if origen and destino and origen != destino:
            resultado = camino_optimo_con_costera(origen, destino, construir_grafo(aristas), Ciudad.obtener_ciudades_costeras())            
            if resultado and 'camino' in resultado:
                nombre_imagen = 'grafo_resaltado.png'
                grafo_a_imagen_marcado(nombre_imagen, resultado['camino'], construir_grafo(aristas))
                imagen = f'img/{nombre_imagen}'

        return {
            'ciudades': ciudades_nombre,
            'resultado': resultado,
            'imagen': imagen
        }
    except Exception:
        return {
            'resultado': None,
            'ciudades': ciudades_nombre,
        }

# Controlador para obtener el grafo completo como imagen
def obtener_grafo():
    aristas = Conexiones.obtener_conexiones()
    grafo = construir_grafo(aristas)
    imagen_grafo = grafo_a_imagen(G=grafo)
    imagen_url = url_for('static', filename=imagen_grafo)
    return {
        'imagen_url': imagen_url
    }