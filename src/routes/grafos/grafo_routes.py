from flask import Blueprint, render_template, request, flash
from controllers.grafos.grafo_controller import obtener_camino_formulario_get, obtener_camino_formulario_post, obtener_grafo
from flask_login import login_required
from utils.generar_pdf.tablas import generar_pdf_rutas

# Blueprint para las rutas de opciones de grafos
# Este archivo maneja las rutas para calcular caminos y visualizar el grafo
camino_formulario_bp = Blueprint('camino_formulario', __name__)
# Blueprint para la información de grafos
# Este blueprint se usa para mostrar información sobre los grafos
info_grafos_bp = Blueprint('info_grafos', __name__)
# Blueprint para visualizar el grafo
# Este blueprint se usa para mostrar el grafo y sus propiedades
grafo_bp = Blueprint('grafo', __name__)

# Ruta para la información de grafos
# Esta ruta muestra información general sobre los grafos y sus propiedades
@info_grafos_bp.route('/info_grafos')
@login_required
def info_grafos():
    return render_template('/grafos/info_grafos.html')

# Ruta para el formulario de cálculo de caminos
# Esta ruta maneja tanto el método GET para mostrar el formulario de cálculo de caminos
@camino_formulario_bp.route('/camino_formulario', methods=['GET', 'POST'])
@login_required
def camino_formulario():
    if request.method == 'GET':
        data = obtener_camino_formulario_get()
        return render_template("/grafos/rutas.html", **data)
    
    elif request.method == 'POST':
        # Generar PDF de rutas
        if 'descargar_pdf' in request.form:
            origen = request.form.get('origen_pdf')
            destino = request.form.get('destino_pdf')
            if origen and destino:
                # Obtener los datos de la ruta calculada
                data = obtener_camino_formulario_post(origen, destino)
                try:
                    imagen_path = data.get('imagen', '')
                    pdf_response = generar_pdf_rutas(origen, destino, data['resultado'], imagen_path)
                    if pdf_response:
                        return pdf_response
                    else:
                        flash('Error al generar el PDF', 'error')
                except Exception:
                    flash(f'Error al generar el PDF', 'error')
                return render_template("/grafos/rutas.html", **data)
        
        # Cálculo normal de ruta
        origen = request.form.get('origen')
        destino = request.form.get('destino')
        
        data = obtener_camino_formulario_post(origen, destino)
        if origen == destino:
            flash('El origen y el destino no pueden ser iguales.', 'error')

        elif data['resultado']['camino'] == []:
            flash('No se encontró un camino entre las ciudades seleccionadas.', 'error')
            return render_template("/grafos/rutas.html", **data)
        return render_template("/grafos/rutas.html", **data)

# Ruta para visualizar el grafo
@grafo_bp.route('/grafo')
@login_required
def grafo():
    data = obtener_grafo()
    return render_template('/grafos/grafo.html', **data)