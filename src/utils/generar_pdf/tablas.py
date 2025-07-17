from xhtml2pdf import pisa
from flask import make_response, render_template, flash, current_app
from datetime import datetime
import os
import base64

# Funcion para generar el PDF de ciudades
# Recibe una lista de ciudades y provincias para incluir en el PDF
def generar_pdf_ciudades(ciudades, provincias):
    try:
        # Renderizar la plantilla HTML con los datos de ciudades y provincias
        html_content = render_template('pdf/ciudades_pdf.html', 
                                     ciudades=ciudades, 
                                     provincias=provincias,
                                     fecha_generacion=datetime.now().strftime("%d/%m/%Y %H:%M"))
        
        response = make_response()
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename=ciudades_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        
        # Generar el PDF a partir del contenido HTML
        pisa_status = pisa.CreatePDF(html_content, dest=response.stream)
        
        # Verificar si hubo errores al generar el PDF
        if pisa_status.err:
            return None
        
        # Return the response containing the PDF
        return response
       
    except Exception:
        flash('Error al generar el PDF de ciudades', 'error')
        return None

# Funcion para generar el PDF de provincias
# Recibe una lista de provincias para incluir en el PDF
def generar_pdf_provincias(provincias):
    try:
        # Renderizar la plantilla HTML con los datos de provincias
        html_content = render_template('pdf/provincias_pdf.html', 
                                     provincias=provincias,
                                     fecha_generacion=datetime.now().strftime("%d/%m/%Y %H:%M"))
        
        response = make_response()
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename=provincias_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        
        # Generar el PDF a partir del contenido HTML
        pisa_status = pisa.CreatePDF(html_content, dest=response.stream)
        
        # Verificar si hubo errores al generar el PDF
        if pisa_status.err:
            return None
        
        # Return the response containing the PDF
        return response
        
    except Exception:
        flash('Error al generar el PDF de provincias', 'error')
        return None

# Funcion para generar el PDF de conexiones
# Recibe una lista de conexiones y ciudades para incluir en el PDF
def generar_pdf_conexiones(conexiones, ciudades):
    try:
        # Renderizar la plantilla HTML con los datos de conexiones y ciudades
        html_content = render_template('pdf/conexiones_pdf.html', 
                                     conexiones=conexiones,
                                     ciudades=ciudades,
                                     fecha_generacion=datetime.now().strftime("%d/%m/%Y %H:%M"))
        
        response = make_response()
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename=conexiones_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        
        # Generar el PDF a partir del contenido HTML
        pisa_status = pisa.CreatePDF(html_content, dest=response.stream)
        
        # Verificar si hubo errores al generar el PDF
        if pisa_status.err:
            return None
        
        # Return the response containing the PDF
        return response
        
    except Exception:
        flash('Error al generar el PDF de conexiones', 'error')
        return None

# Funcion para generar el PDF de rutas
# Recibe origen, destino, resultado y la ruta de la imagen para incluir en el PDF
def generar_pdf_rutas(origen, destino, resultado, imagen_path):
    try:
        # Convertir imagen a base64 para incluirla en el PDF
        imagen_base64 = None
        if imagen_path:
            try:
                # Construir la ruta completa de la imagen
                ruta_completa = os.path.join(current_app.static_folder, imagen_path)
                if os.path.exists(ruta_completa):
                    with open(ruta_completa, "rb") as image_file:
                        imagen_base64 = base64.b64encode(image_file.read()).decode('utf-8')
            except Exception as e:
                print(f"Error al cargar imagen: {e}")
        
        # Renderizar la plantilla HTML con los datos de la ruta y la imagen en base64
        html_content = render_template('pdf/rutas_pdf.html', 
                                     origen=origen,
                                     destino=destino,
                                     resultado=resultado,
                                     imagen_base64=imagen_base64,
                                     fecha_generacion=datetime.now().strftime("%d/%m/%Y %H:%M"))
        
        response = make_response()
        response.headers['Content-Type'] = 'application/pdf'
        response.headers['Content-Disposition'] = f'attachment; filename=ruta_{origen}_{destino}_{datetime.now().strftime("%Y%m%d_%H%M%S")}.pdf'
        
        # Generar el PDF a partir del contenido HTML
        pisa_status = pisa.CreatePDF(html_content, dest=response.stream)
        
        # Verificar si hubo errores al generar el PDF
        if pisa_status.err:
            return None
        
        # Return the response containing the PDF
        return response
        
    except Exception as e:
        print(f"Error al generar PDF de rutas: {e}")
        flash('Error al generar el PDF de rutas', 'error')
        return None
