# routes/borrar.py
from flask import Blueprint, request, flash, redirect, render_template, url_for
import sqlite3

borr = Blueprint('borr', __name__)  

DATABASE = 'creditos.db'

def get_db():
    return sqlite3.connect(DATABASE)

@borr.route('/borrar/<int:id>', methods=['GET', 'POST'])
def borrar(id):
    if id:
        db = get_db()
        cursor = db.cursor()
        flash(f"Se ha eliminado el registro con el ID {id}")

        # Consulta SQL corregida
        cursor.execute("DELETE FROM creditos WHERE id = ?", (id,))

        db.commit()  
        db.close()  
        return redirect(url_for('listar.lista'))  
    else:
        return render_template('listar.html')  # En caso de error, muestra la página listar
