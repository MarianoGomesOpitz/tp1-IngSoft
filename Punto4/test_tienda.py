from producto import Producto
from tienda import Tienda
import pytest
from unittest.mock import Mock

##Punto 4

@pytest.fixture
def tienda_con_productos():
    tienda = Tienda()
    leche = Producto("leche", 1.5, "Lacteos")
    queso = Producto("queso", 2.8, "Lacteos")
    tienda.agregar_producto(leche)
    tienda.agregar_producto(queso)
    return tienda 

def test_agrega_producto(tienda_con_productos):
    assert len(tienda_con_productos.inventario)==2
    
def test_busca_producto(tienda_con_productos):
    with pytest.raises(Exception)as e:
        prod=tienda_con_productos.buscar_producto("Zeta")
    assert str(e.value) == "Se produjo un error, nombre no encontrado"
