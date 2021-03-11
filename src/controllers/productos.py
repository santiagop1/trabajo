from flask import render_template, request, redirect, url_for
from src import app
from src.models.productos import ProductosModel
productosModel = ProductosModel() 
@app.route('/productos')
def productos():
    
    productos = productosModel.traerTodos()
    #print(productos)
    return render_template('productos/index.html', productos = productos)

@app.route('/productos/crear', methods=['GET','POST'])
def crear_producto():
    if request.method == 'GET':
        return render_template('productos/crear.html')
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precioCompra = request.form.get('precioCompra')
    precioVenta = request.form.get('precioVenta')
    ganancia = request.form.get('ganancia')
    estado = request.form.get('estado')
    #print(estado)
    productosModel = ProductosModel() 
    productos = productosModel.crear(nombre, descripcion, precioCompra, precioVenta, ganancia, estado)
    return redirect(url_for('productos'))

@app.route('/productos/editar/<id>', methods= ['GET','POST'])
def editar_producto(id):
    if request.method == 'GET':
        
        producto = productosModel.traerUno(id)
        
        return render_template('productos/editar.html', producto = producto)
    
    nombre = request.form.get('nombre')
    descripcion = request.form.get('descripcion')
    precioCompra = request.form.get('precioCompra')
    precioVenta = request.form.get('precioVenta')
    ganancia = request.form.get('ganancia')
    estado = request.form.get('estado')
    

    productosModel.editar(nombre, descripcion, precioCompra, precioVenta, ganancia, estado, id)
    
    print(nombre, descripcion, precioCompra, precioVenta, ganancia, estado)
    return redirect(url_for('productos')) 