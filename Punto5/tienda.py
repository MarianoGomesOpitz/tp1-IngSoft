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
    
    def aplicar_descuento(self, nombre, porc):
        if porc<0 or porc>100:
            return False
        else:
            producto = self.buscar_producto(nombre)
            if producto:
                nuevo_precio = producto.precio * (1 - porc / 100)
                producto.actualizar_precio(nuevo_precio)
                return True
            return False
        
    ##Referido al carrito 

    def calcular_total_carrito(self,lista):
        total=0
        for nombre in lista:
            producto = self.buscar_producto(nombre)
            total+=producto.precio
        return total