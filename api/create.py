from flask import Blueprint, jsonify, request
import sqlite3

apiCreate = Blueprint('Create', __name__)

DATABASE = 'creditos.db'

def get_db():
    return sqlite3.connect(DATABASE)

@apiCreate.route('/api/crear', methods=['POST'])
def crear_credito():
    try:
        # Obtener datos de la solicitud
        data = request.get_json()

        # Extraer los valores
        cliente = data.get('cliente')
        tasa_interes = data.get('tasa_interes')
        plazo = data.get('plazo')
        fecha_otorgamiento = data.get('fecha_otorgamiento')
        monto = data.get('monto')

        # Validar que no haya datos vacíos
        if not all([cliente, tasa_interes, plazo, fecha_otorgamiento, monto]):
            return jsonify({"error": "Todos los campos son obligatorios"}), 400

        # Conectar a la base de datos e insertar el nuevo crédito
        db = get_db()
        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO creditos (cliente, tasa_interes, plazo, fecha_otorgamiento, monto) 
            VALUES (?, ?, ?, ?, ?)
        """, (cliente, tasa_interes, plazo, fecha_otorgamiento, monto))
        
        db.commit()
        db.close()

        return jsonify({"mensaje": "Crédito creado exitosamente"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500