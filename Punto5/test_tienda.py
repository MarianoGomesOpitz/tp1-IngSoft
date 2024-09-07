from producto import Producto
from tienda import Tienda
import pytest
from unittest.mock import Mock

##Punto 5

@pytest.fixture
def tienda_con_productos():
    tienda = Tienda()
    leche = Producto("leche", 1.5, "Lacteos")
    queso = Producto("queso", 2.8, "Lacteos")
    pan = Producto("pan", 1.0, "Panadería")
    jamon_crudo= Producto ("jamon_crudo", 2.0, "Fiambres")
    galleta_salvado= Producto ("galleta_salvado", 5.4, "Galletas")
    tienda.agregar_producto(leche)
    tienda.agregar_producto(queso)
    tienda.agregar_producto(pan)
    tienda.agregar_producto(jamon_crudo)
    tienda.agregar_producto(galleta_salvado)
    return tienda 

def test_calcular_total_carrito(tienda_con_productos):
    tienda_con_productos.aplicar_descuento("leche", 10)
    tienda_con_productos.aplicar_descuento("jamon_crudo", 10)
    carrito= ["leche", "queso", "pan", "jamon_crudo","galleta_salvado"]
    total = tienda_con_productos.calcular_total_carrito(carrito)
    assert round(total,2) == 12.35  ##El 12.35 es la sumatoria de todos los productos con el descuento correspondiente
    


## Una situación de desarrollo en la que las pruebas sean de integración ascendente es uno en el que se desarrolla 
## cada módulo de nivel inferior y al tenerlo probado hasta un punto satisfactorio, se prosigue con un módulo de nivel 
## superior que utiliza ese módulo inferior.
## Un ejemplo puede ser el de este mismo TP. Primero se desarrolla el objeto Producto con todos las funcionalidades que le
## corresponden, se las prueba de manera exhaustiva para corrobar que funcione correctamente, y encontrar y solucionar posibles
## errores de funcionamiento. Luego se continua con la Tienda, que utiliza al Producto y a sus funciones para sí mismas.
## Se realizan pruebas que verifiquen su funcionamiento, y al ya saber que el Producto funciona correctamente, los posibles
## errores que pueden aparecer son del funcionamiento de la Tienda, o de implementación del Producto en la Tienda. Para el final
## realizar la función de calcular la compra que utiliza todas las funciones de la Tienda.