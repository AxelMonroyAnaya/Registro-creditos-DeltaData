from flask import Blueprint, jsonify, request
import sqlite3

apiGet = Blueprint('api', __name__)

DATABASE = 'creditos.db'

def get_db():
    return sqlite3.connect(DATABASE)

@apiGet.route('/api/creditos', methods=['GET'])
def obtener_creditos():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM creditos")
    creditos = cursor.fetchall()  
    db.close()

    # Convertir a JSON
    lista_creditos = [
        {"id": row[0], "cliente": row[1], "tasa_interes": row[2], "plazo": row[3], "fecha_otorgamiento": row[4], "monto": row[5]}
        for row in creditos
    ]
    
    return jsonify(lista_creditos)

 