from flask import Blueprint, request,flash,redirect,render_template,url_for
import sqlite3
registrar = Blueprint('registrar', __name__)

DATABASE = 'creditos.db'

def get_db():
    return sqlite3.connect(DATABASE)

@registrar.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        monto = request.form['monto']
        tasa = request.form['tasa']
        plazo = request.form['plazo']
        fecha = request.form['fecha']
        db = get_db()
        cursor = db.cursor()
        cursor.execute("INSERT INTO creditos (cliente, tasa_interes, plazo, fecha_otorgamiento, monto) VALUES (?, ?, ?, ?, ?)",
                       (nombre, tasa, plazo, fecha, monto))
        db.commit()  # Guardamos los cambios en la base de datos
        flash(f"se ha guardado correctamente el registro de {nombre} el dia {fecha}")
        return redirect(url_for('listar.lista'))  # Redirige a la página principal
    else:
        return render_template('registro.html')  # Redirige a la página principal)
