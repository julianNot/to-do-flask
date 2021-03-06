''' Conexion a la base datos '''

import mysql.connector
import click #comandos terminal
from flask import current_app, g 
from flask.cli import with_appcontext #acceder a las variables
from .schema import instructions #scripts necesarios BD(consultas)

def get_db():
    if 'db' not in g:
        #Variables de configuracion (conexion a bd)
        g.db = mysql.connector.connect(
            host=current_app.config['DATABASE_HOST'],
            user=current_app.config['DATABASE_USER'],
            passwd=current_app.config['DATABASE_PASSWORD'],
            database=current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True) #acceder al cursor
    return g.db, g.c

def close_db(e=None):
    db = g.pop('db', None) #quita db de g

    if db is not None:
        db.close()
    
def init_db():
    db, c = get_db()

    for i in instructions:
        c.execute(i)

    db.commit()

@click.command('init-db') #ejecutar desde la terminal
@with_appcontext #acceder a las variables de config
def init_db_command():
    init_db()
    click.echo('Base de datos inicializada')   

def init_app(app):
    app.teardown_appcontext(close_db) #ejecuta funciones
    app.cli.add_command(init_db_command) #escribir comando