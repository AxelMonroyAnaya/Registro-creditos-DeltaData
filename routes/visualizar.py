import matplotlib.pyplot as plt
import pandas as pd 
import sqlite3 
from flask import render_template, Blueprint
import os
DATABASE = 'creditos.db'

grafica = Blueprint('grafica',__name__)

@grafica.route('/grafica')
def mostrar_grafica():
    conn = sqlite3.connect(DATABASE)

    query = "SELECT * FROM creditos order by fecha_otorgamiento ASC"
    df = pd.read_sql_query(query, conn)
    print(df)
    df['fecha_otorgamiento'] = pd.to_datetime(df['fecha_otorgamiento'])

    plt.style.use('ggplot')

    df['año_mes'] = df['fecha_otorgamiento'].dt.to_period('M')  # Agrupa por Año-Mes
    conteo_meses = df.groupby('año_mes').size()

    # Graficar los créditos otorgados por mes
    plt.figure(figsize=(10, 5))
    plt.plot(conteo_meses.index.astype(str), conteo_meses.values, marker='x', linestyle='-')

    # Personalización del gráfico
    plt.xlabel("Fecha (Año-Mes)")
    plt.ylabel("Total de Créditos Otorgados")
    plt.title("Créditos Otorgados por Mes")
    plt.xticks(rotation=45)  

    img_path = os.path.join("static/img", "grafica.png")
    plt.savefig(img_path)  # Guardar la imagen en la carpeta static
    plt.close()  

    return render_template('grafica.html', img_url="img/grafica.png")
