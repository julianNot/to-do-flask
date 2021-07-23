# to-do-flask

_Applicacion de lista de tareas web (backend), desarrollada con Flask y base de datos MySql.
CRUD de notas, manejo de registro de usuarios_

##  Iniciando

_Crear entorno virtual_
```
virtualenv env
```
_Activar entorno virtual (env)_

```
source env/bin/activate
```
_Iniciar la Base de Datos_

```
flask init-db
```

### Requisitos

_Ingresar las variables de entorno de la Base de Datos_
```
export FLASK_DATABASE_HOST='host_de_tu_base_de_datos'
export FLASK_DATABASE_PASSWORD='contraseña_usuario_conectado_a_BD'
export FLASK_DATABASE_USER='nombre_usuario_de_BD'
export FLASK_DTABASE='nombre_de_la_BD'
```
_Variables de entorno de Flask_

```
export FLASK_DEBUG=1
export FLASK_APP='nombre_carpeta_con_codigo_fuente'
```
_La App se ejecutara en localhost_
