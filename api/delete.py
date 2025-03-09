from flask import Blueprint, jsonify, request
import sqlite3

apiDelete = Blueprint('delete', __name__)

DATABASE = 'creditos.db'

def get_db():
    return sqlite3.connect(DATABASE)

@apiDelete.route('/api/creditos/<int:id>', methods=['DELETE'])
def obtener_creditos(id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(f"DELETE  FROM creditos where id={id}")
    creditos = cursor.fetchall()  
    db.commit()
    db.close()

    # Convertir a JSON
    lista_creditos = [
        {"id": row[0], "cliente": row[1], "tasa_interes": row[2], "plazo": row[3], "fecha_otorgamiento": row[4], "monto": row[5]}
        for row in creditos
    ]
    
    return jsonify(lista_creditos)

 