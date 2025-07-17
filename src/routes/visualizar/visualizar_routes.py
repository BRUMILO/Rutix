from flask import Blueprint, render_template, request, redirect, url_for, flash
from controllers.visualizar.vizualizar_controller import obtener_provincias_controller, obtener_ciudades_controller, obtener_conexiones_controller
from controllers.agregar.agregar_controller import agregar_ciudad_controller, agregar_provincia_controller, agregar_ruta_controller
from controllers.eliminar.eliminar_controller import eliminar_provincia_controller, eliminar_ciudad_controller, eliminar_conexion_controller
from controllers.editar.editar_controller import editar_provincia_controller, editar_ciudad_controller, editar_conexion_controller
from utils.generar_pdf.tablas import generar_pdf_ciudades, generar_pdf_provincias, generar_pdf_conexiones

# Blueprint para las rutas de visualización
# Este archivo maneja las rutas para visualizar ciudades, provincias y conexiones
visualizar_ciudades_bp = Blueprint('visualizar_ciudades', __name__)
# Blueprint para visualizar provincias
# Permite agregar, editar y eliminar provincias, así como descargar un PDF con la lista de provincias
visualizar_provincias_bp = Blueprint('visualizar_provincias', __name__)
# Blueprint para visualizar conexiones
# Permite agregar, editar y eliminar conexiones, así como descargar un PDF con la lista de conexiones
visualizar_conexiones_bp = Blueprint('visualizar_conexiones', __name__)

# Ruta para visualizar ciudades
# Permite agregar, editar y eliminar ciudades, así como descargar un PDF con la lista de ciudades
@visualizar_ciudades_bp.route('/visualizar_ciudades', methods=['GET', 'POST'])
def visualizar_ciudades():
    if request.method == 'POST':
        # Agregar ciudad
        if 'agregar_ciudad' in request.form:
            nombre = request.form.get('nombre_ciudad')
            provincia_id = request.form.get('provincia_id')
            costera = request.form.get('costera') == '1'
            if nombre and provincia_id:
                try:
                    agregar_ciudad_controller(nombre, int(provincia_id), costera)
                except Exception:
                    flash(f'Error al agregar ciudad', 'error')
                return redirect(url_for('visualizar_ciudades.visualizar_ciudades'))
        
        # Editar ciudad
        elif 'editar_ciudad' in request.form:
            ciudad_id = request.form.get('ciudad_id')
            nuevo_nombre = request.form.get('nuevo_nombre_ciudad')
            nueva_provincia_id = request.form.get('nueva_provincia_id')
            nueva_costera = request.form.get('nueva_costera') == '1'
            if ciudad_id and nuevo_nombre and nueva_provincia_id:
                try:
                    if editar_ciudad_controller(int(ciudad_id), nuevo_nombre, int(nueva_provincia_id), nueva_costera):
                        flash('Ciudad editada exitosamente', 'success')
                    else:
                        flash('Error al editar ciudad', 'error')
                except Exception:
                    flash(f'Error al editar ciudad', 'error')
                return redirect(url_for('visualizar_ciudades.visualizar_ciudades'))
        
        # Eliminar ciudad
        elif 'eliminar_ciudad' in request.form:
            ciudad_id = request.form.get('ciudad_id')
            if ciudad_id:
                try:
                    if eliminar_ciudad_controller(int(ciudad_id)):
                        flash('Ciudad eliminada exitosamente', 'success')
                    else:
                        flash('Error al eliminar ciudad', 'error')
                except Exception:
                    flash(f'Error al eliminar ciudad', 'error')
                return redirect(url_for('visualizar_ciudades.visualizar_ciudades'))
        
        elif 'descargar_pdf' in request.form:
            # Generar y descargar PDF de ciudades
            try:
                provincias = obtener_provincias_controller()
                ciudades = obtener_ciudades_controller()
                pdf_response = generar_pdf_ciudades(ciudades['ciudades'], provincias['provincias'])
                if pdf_response:
                    return pdf_response
                else:
                    flash('Error al generar el PDF', 'error')
            except Exception:
                flash(f'Error al generar el PDF', 'error')

    provincias = obtener_provincias_controller()
    ciudades = obtener_ciudades_controller()
    return render_template('visualizar/ciudades.html', **ciudades, **provincias)

# Ruta para visualizar provincias
# Permite agregar, editar y eliminar provincias, así como descargar un PDF con la lista de provincias
@visualizar_provincias_bp.route('/visualizar_provincias', methods=['GET', 'POST'])
def visualizar_provincias():
    if request.method == 'POST':
        # Agregar provincia
        if 'agregar_provincia' in request.form:
            nombre = request.form.get('nombre_provincia')
            if nombre:
                try:
                    agregar_provincia_controller(nombre)
                except Exception:
                    flash(f'Error al agregar provincia', 'error')
                return redirect(url_for('visualizar_provincias.visualizar_provincias'))
        
        # Editar provincia
        elif 'editar_provincia' in request.form:
            provincia_id = request.form.get('provincia_id')
            nuevo_nombre = request.form.get('nuevo_nombre_provincia')
            if provincia_id and nuevo_nombre:
                try:
                    if editar_provincia_controller(int(provincia_id), nuevo_nombre):
                        flash('Provincia editada exitosamente', 'success')
                    else:
                        flash('Error al editar provincia', 'error')
                except Exception:
                    flash(f'Error al editar provincia', 'error')
                return redirect(url_for('visualizar_provincias.visualizar_provincias'))
        
        # Eliminar provincia
        elif 'eliminar_provincia' in request.form:
            provincia_id = request.form.get('provincia_id')
            if provincia_id:
                try:
                    if eliminar_provincia_controller(int(provincia_id)):
                        flash('Provincia eliminada exitosamente', 'success')
                    else:
                        flash('Error al eliminar provincia', 'error')
                except Exception:
                    flash(f'Error al eliminar provincia', 'error')
                return redirect(url_for('visualizar_provincias.visualizar_provincias'))
        
        # Descargar PDF de provincias
        elif 'descargar_pdf' in request.form:
            try:
                provincias = obtener_provincias_controller()
                pdf_response = generar_pdf_provincias(provincias['provincias'])
                if pdf_response:
                    return pdf_response
                else:
                    flash('Error al generar el PDF', 'error')
            except Exception:
                flash(f'Error al generar el PDF', 'error')
            
    provincias = obtener_provincias_controller()
    return render_template('visualizar/provincias.html', **provincias)

# Ruta para visualizar conexiones
# Permite agregar, editar y eliminar conexiones, así como descargar un PDF con la lista de conexiones
@visualizar_conexiones_bp.route('/visualizar_conexiones', methods=['GET', 'POST'])
def visualizar_conexiones():
    if request.method == 'POST':
        # Agregar ruta
        if 'agregar_ruta' in request.form:
            origen_id = request.form.get('origen_id')
            destino_id = request.form.get('destino_id')
            distancia = request.form.get('distancia')
            if origen_id and destino_id and distancia:
                try:
                    agregar_ruta_controller(origen_id, destino_id, float(distancia))
                except Exception:
                    flash(f'Error al agregar ruta', 'error')
                return redirect(url_for('visualizar_conexiones.visualizar_conexiones'))
        
        # Editar conexión
        elif 'editar_conexion' in request.form:
            conexion_id = request.form.get('conexion_id')
            nuevo_origen_id = request.form.get('nuevo_origen_id')
            nuevo_destino_id = request.form.get('nuevo_destino_id')
            nueva_distancia = request.form.get('nueva_distancia')
            if conexion_id and nuevo_origen_id and nuevo_destino_id and nueva_distancia:
                try:
                    if editar_conexion_controller(int(conexion_id), int(nuevo_origen_id), int(nuevo_destino_id), float(nueva_distancia)):
                        flash('Conexión editada exitosamente', 'success')
                    else:
                        flash('Error al editar conexión', 'error')
                except Exception:
                    flash(f'Error al editar conexión', 'error')
                return redirect(url_for('visualizar_conexiones.visualizar_conexiones'))
        
        # Eliminar conexión
        elif 'eliminar_conexion' in request.form:
            conexion_id = request.form.get('conexion_id')
            if conexion_id:
                try:
                    if eliminar_conexion_controller(int(conexion_id)):
                        flash('Conexión eliminada exitosamente', 'success')
                    else:
                        flash('Error al eliminar conexión', 'error')
                except Exception:
                    flash(f'Error al eliminar conexión', 'error')
                return redirect(url_for('visualizar_conexiones.visualizar_conexiones'))
        
        # Descargar PDF de conexiones
        elif 'descargar_pdf' in request.form:
            try:
                ciudades = obtener_ciudades_controller()
                conexiones = obtener_conexiones_controller()
                pdf_response = generar_pdf_conexiones(conexiones, ciudades)
                if pdf_response:
                    return pdf_response
                else:
                    flash('Error al generar el PDF', 'error')
            except Exception:
                flash(f'Error al generar el PDF', 'error')

    ciudades = obtener_ciudades_controller()
    conexiones = obtener_conexiones_controller()
    return render_template('visualizar/conexiones.html', conexiones = conexiones, **ciudades)
