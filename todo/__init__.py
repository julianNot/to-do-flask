''' Archivo __init__.py hace que python 
interprete la carpeta como un modulo'''

import os 
from flask import Flask

def create_app():
    app = Flask(__name__) #instancia clase flask

    '''Variables de entorno'''
    app.config.from_mapping(
        SECRET_KEY='mikey', #llave de sesiones(cookie)
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),#Donde se encuentra la BD
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'),
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'),
        DATABASE=os.environ.get('FLASK_DATABASE'),
    )

    from . import db
    
    db.init_app(app)

    from . import auth
    from . import todo
    """ Registro de blueprints """
    app.register_blueprint(auth.bp)
    app.register_blueprint(todo.bp)

    @app.route('/hola')
    def hola():
        return 'hola'
    
    return app
