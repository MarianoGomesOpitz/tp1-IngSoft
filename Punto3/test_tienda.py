from producto import Producto
from tienda import Tienda
import pytest
from unittest.mock import Mock

##Punto 3

def agregarProductos(tienda):               ##Funcion que da una tienda ya armada
    leche = Producto("leche", 1.5, "Lacteos")  
    queso = Producto("queso", 2.8, "Lacteos")
    tienda.agregar_producto(leche)
    tienda.agregar_producto(queso)
    
def test_aplicar_descuento_mock():
    ##Crear un mock de la clase Producto
    mock_producto=Mock()
    mock_producto.nombre = "leche"
    mock_producto.precio = 100.0
    mock_producto.categoria="Lacteos"
    
    ##Utilizar el mock para testear la funcion aplicar_descuento
    tienda= Tienda()
    tienda.agregar_producto(mock_producto)
    assert tienda.aplicar_descuento("leche", 50)
