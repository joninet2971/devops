from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/vehiculos_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models import Marca, Tipo 

listadoProductos = [
    {
    'nombre': 'Harina 000',
    'categoria': 'harinas / salvados'
    },
    {
    'nombre': 'Harina Integral',
    'categoria': 'harinas / salvados'
    },
    {
    'nombre': 'Aceite Soja',
    'categoria': 'Aceites'
    },
    {
    'nombre': 'Aceite Girasol',
    'categoria': 'Aceites'
    },
]

@app.route("/")
def index():
    return render_template(
        'index.html',
        )

@app.route("/productos")
def mostrarProductos():
    return render_template('productos.html', productos = listadoProductos)


@app.route("/agregarproducto" , methods=['POST', 'GET'])
def agregarProducto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        producto = {
            'nombre': nombre,
            'categoria': categoria
        }
        listadoProductos.append(producto)
    print(listadoProductos)
    return render_template('agregar_producto.html')