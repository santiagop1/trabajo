from src.config.db import DB
class ProductosModel():
    def traerTodos(self):
        cursor = DB.cursor()
        cursor.execute('select * from productos')
        productos = cursor.fetchall()
        cursor.close()
        
        return productos
    
    def traerUno(self,id):
        cursor = DB.cursor()
        cursor.execute('select * from productos where id=?',(id,))
        producto = cursor.fetchone()
        cursor.close
        return producto

    def crear(self, nombre, descripcion, precioCompra, precioVenta, ganancia, estado):
        cursor= DB.cursor()

        cursor.execute('insert into productos(nombre, descripcion, precio_compra, precio_venta, ganancia, estado) values(?,?,?,?,?,?)',(nombre, descripcion, precioCompra, precioVenta, ganancia, estado,))
        cursor.close()

    def editar(self, nombre, descripcion, precioCompra, precioVenta, ganancia, estado, id):
        cursor= DB.cursor()

        cursor.execute('UPDATE productos SET nombre= ?, descripcion= ?, precio_compra= ?, precio_venta= ?, ganancia= ?, estado= ? WHERE id = ?',(nombre, descripcion, precioCompra, precioVenta, ganancia, estado, id))