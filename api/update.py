from flask import Blueprint, jsonify, request
import sqlite3

apiUpdate = Blueprint('update', __name__)

DATABASE = 'creditos.db'

def get_db():
    return sqlite3.connect(DATABASE)

@apiUpdate.route('/api/update/<int:id>', methods=['PUT'])
def actualizar_credito(id):
    datos = request.get_json()

    # Validar que al menos un campo esté presente
    campos_permitidos = ["cliente", "tasa_interes", "plazo", "fecha_otorgamiento", "monto"]
    datos_actualizar = {key: datos[key] for key in datos if key in campos_permitidos}

    if not datos_actualizar:
        return jsonify({"error": "Debes enviar al menos un campo válido para actualizar"}), 400

    try:
        db = get_db()
        cursor = db.cursor()

        # Construir la consulta dinámicamente
        set_clause = ", ".join([f"{campo} = ?" for campo in datos_actualizar.keys()])
        valores = list(datos_actualizar.values())
        valores.append(id)

        cursor.execute(f"""
            UPDATE creditos
            SET {set_clause}
            WHERE id = ?
        """, valores)

        if cursor.rowcount == 0:
            return jsonify({"error": "Crédito no encontrado"}), 404

        db.commit()
        db.close()

        return jsonify({"mensaje": "Crédito actualizado exitosamente"}), 200

    except sqlite3.Error as e:
        return jsonify({"error": f"Error en la base de datos: {str(e)}"}), 500
