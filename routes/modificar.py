from flask import Blueprint, request,flash,redirect,render_template,url_for
import sqlite3

modificar = Blueprint('modificar', __name__)

DATABASE = 'creditos.db'

def get_db():
    return sqlite3.connect(DATABASE)

@modificar.route('/modificar/<int:id>', methods=['GET', 'POST'])
def mod(id):
    db = get_db()
    if request.method == 'POST':
        nombre = request.form['nombre']
        monto = request.form['monto']
        tasa = request.form['tasa']
        plazo = request.form['plazo']
        fecha = request.form['fecha']
        db = get_db()
        cursor = db.cursor()
        flash(f"se ha guardado correctamente el registro de {nombre} el dia {fecha}")
        cursor.execute("""
                    UPDATE creditos 
                    SET cliente = ?, tasa_interes = ?, plazo = ?, fecha_otorgamiento = ?, monto = ? 
                    WHERE id = ?
                """, (nombre, tasa, plazo, fecha, monto, id))
        db.commit()
        db.close()
        return redirect(url_for('listar.lista'))  
    else:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM creditos WHERE id = {id}")
        creditos = cursor.fetchall()
        db.close()
        return render_template('registro.html',credito = creditos[0])
