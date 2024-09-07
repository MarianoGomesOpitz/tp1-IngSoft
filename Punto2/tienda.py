from producto import Producto

class Tienda:
    def __init__(self):
        self.inventario = []
    
    def agregar_producto(self, producto):
        self.inventario.append(producto)
        
    def buscar_producto(self, nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                return producto
        raise Exception(f"Se produjo un error, nombre no encontrado")
        

    def eliminar_producto(self, nombre):
        for producto in self.inventario:
            if producto.nombre == nombre:
                self.inventario.remove(producto)
                return True
        raise Exception(f"Se produjo un error, no se encontro el producto a eliminar")