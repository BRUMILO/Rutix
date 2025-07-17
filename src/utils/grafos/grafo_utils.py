import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import networkx as nx
import os

# Construir el grafo dirigido y ponderado
# Recibe una lista de aristas (tuplas de origen, destino, costo)
# Retorna un objeto de grafo de NetworkX
def construir_grafo(aristas):
    G = nx.Graph()
    for origen, destino, costo in aristas:
        G.add_edge(origen, destino, weight=costo)
    return G

# Función para renderizar el grafo como imagen
# Esta función recibe un nombre de archivo y un grafo G
# Retorna el nombre del archivo de imagen generado
def grafo_a_imagen(nombre_archivo='grafo.png', G=None):
    pos = nx.spring_layout(G, seed=8)
    pesos = nx.get_edge_attributes(G, 'weight')

    fig, ax = plt.subplots(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color="#0aa4e6", node_size=2000, font_weight='bold', arrows=True)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)

    ruta_archivo = os.path.join('static/img', nombre_archivo)

    plt.savefig(ruta_archivo, format='png')
    plt.close()

    return nombre_archivo

# Función para renderizar el grafo con el camino marcado
# Esta función recibe un nombre de archivo, un camino y el grafo G
# Retorna el nombre del archivo de imagen generado
def grafo_a_imagen_marcado(nombre_archivo='grafo.png', camino=None, G=None):
    pos = nx.spring_layout(G, seed=8)
    pesos = nx.get_edge_attributes(G, 'weight')

    fig, ax = plt.subplots(figsize=(10, 7))
    
    nx.draw(G, pos, with_labels=True, node_color="#0aa4e6", node_size=2000,
            font_weight='bold', arrows=True, edge_color='gray')

    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)

    if camino and len(camino) >= 2:
        aristas_camino = list(zip(camino, camino[1:]))

        nx.draw_networkx_edges(G, pos, edgelist=aristas_camino, edge_color="#80fa6d", width=4, arrows=True)

    nx.draw_networkx_edge_labels(G, pos, edge_labels=pesos)
    ruta_archivo = os.path.join('static/img', nombre_archivo)
    plt.savefig(ruta_archivo, format='png')
    plt.close()

    return nombre_archivo

# Función para calcular el camino óptimo con costeras
# Retorna un diccionario con el camino, costo y si contiene costeras
def camino_optimo_con_costera(origen, destino, G, COSTERAS):
    try:
        camino = nx.dijkstra_path(G, origen, destino, weight='weight')
        costo = nx.dijkstra_path_length(G, origen, destino, weight='weight')

        contiene_costera = any(ciudad in COSTERAS for ciudad in camino)
        return {
            "camino": camino,
            "costo": costo,
            "valido": contiene_costera
        }
    except nx.NetworkXNoPath:
        return {
            "camino": [],
            "costo": None,
            "valido": False
        }
