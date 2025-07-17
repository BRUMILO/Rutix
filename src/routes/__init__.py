from .home_routes import home_bp, menu_bp
from .users.user_routes import login_bp, register_bp, logout_bp
from .grafos.grafo_routes import camino_formulario_bp, grafo_bp, info_grafos_bp
from .visualizar.visualizar_routes import visualizar_ciudades_bp, visualizar_provincias_bp, visualizar_conexiones_bp
from .advertencia.advertencias_routes import error_admins_bp

def register_blueprints(app):
    # Base
    app.register_blueprint(home_bp)
    app.register_blueprint(menu_bp)
    
    # BP users
    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(logout_bp)
    
    # BP visualizar
    app.register_blueprint(visualizar_ciudades_bp)
    app.register_blueprint(visualizar_provincias_bp)
    app.register_blueprint(visualizar_conexiones_bp)
    
    # BP opciones grafos
    app.register_blueprint(info_grafos_bp)
    app.register_blueprint(camino_formulario_bp)
    app.register_blueprint(grafo_bp)
    
    #Errores
    app.register_blueprint(error_admins_bp)