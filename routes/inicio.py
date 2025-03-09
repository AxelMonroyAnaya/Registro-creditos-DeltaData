from flask import Blueprint, render_template

inicio = Blueprint('index', __name__)

@inicio.route('/')
def index():
    return render_template('index.html')