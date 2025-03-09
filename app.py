from flask import Flask
from routes.modificar import modificar
from routes.inicio import inicio
from routes.listar import listar
from routes.registro import registrar
from routes.borrar import borr
from routes.visualizar import grafica
from api.read import apiGet as read
from api.create import apiCreate as create
from api.update import apiUpdate
from api.delete import apiDelete

app = Flask(__name__)
app.secret_key = 'clave_secreta_flask'

app.register_blueprint(inicio, url_prefix='/')
app.register_blueprint(listar, url_prefix='/listar')
app.register_blueprint(registrar, url_prefix='/registrar')
app.register_blueprint(modificar, url_prefix='/modificar')
app.register_blueprint(borr, url_prefix='/borrar')
app.register_blueprint(grafica, url_prefix = '/grafica')
app.register_blueprint(read, url_prefix = '/apiGet')
app.register_blueprint(create, url_prefix = '/apiCreate')
app.register_blueprint(apiUpdate, url_prefix = '/apiUpdate')
app.register_blueprint(apiDelete, url_prefix = '/apiDelete')




if __name__ == '__main__':
    app.run(debug=True)