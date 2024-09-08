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
