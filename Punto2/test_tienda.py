from producto import Producto
from tienda import Tienda
import pytest

##Punto 2

def agregarProductos(tienda):               ##Funcion que da una tienda ya armada
    leche = Producto("leche", 1.5, "Lacteos")  
    queso = Producto("queso", 2.8, "Lacteos")
    tienda.agregar_producto(leche)
    tienda.agregar_producto(queso)
    
def test_busca_producto():
    tienda = Tienda()
    agregarProductos(tienda)
    with pytest.raises(Exception)as e:
        prod=tienda.buscar_producto("Zeta")
    assert str(e.value) == "Se produjo un error, nombre no encontrado"
    
def test_elimina_producto():
    tienda = Tienda()
    agregarProductos(tienda)
    with pytest.raises(Exception)as e:
        prod=tienda.eliminar_producto("Zeta")
    assert str(e.value) == "Se produjo un error, no se encontro el producto a eliminar"
    
def test_actualiza_producto():
    leche= Producto("Leche", 1.2, "Lacteos")
    with pytest.raises(Exception)as e:
        leche.actualizar_precio(-1)
    assert str(e.value) =="El valor recibido es negativo"
