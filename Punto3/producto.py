class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, precio):
        if(precio>=0):
            self.precio=precio
            return None
        else:
            raise Exception(f"El valor recibido es negativo")