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
    
## En lo que va del tp, se puede identificar que los drivers son aquellos modulos que empiezan por "test_",
## que sirven para probar los módulos.
## En cambio, la aparición de resguardos se da en este ejercicio con la utilización de mocks, para simular el
## valor de retorno de un módulo.

## Un mock es un objeto simulado que reemplaza un componente o dependencia real del código durante una prueba. 
## Los mocks se utilizan para aislar la unidad de código que se está probando, asegurando que las pruebas no 
## dependan de otros componentes externos o de comportamientos impredecibles.
## Otros nombres por los que se le conoce a los mocks son resguardos, stubs, spy, fake, patch.