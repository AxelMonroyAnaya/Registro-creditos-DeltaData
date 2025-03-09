from flask import Blueprint, render_template
import sqlite3

listar = Blueprint('listar', __name__)

DATABASE = 'creditos.db'
def get_db():
    return sqlite3.connect(DATABASE)

@listar.route('/listar')
def lista():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM creditos ORDER BY fecha_otorgamiento DESC')
    creditos = cursor.fetchall()
    db.close()
    return render_template('listar.html',credito = creditos)