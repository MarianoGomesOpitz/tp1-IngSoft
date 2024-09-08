from producto import Producto
from tienda import Tienda

##Punto 1

def agregarProductos(tienda):               ##Funcion que da una tienda ya armada
    leche = Producto("leche", 1.5, "Lacteos")  
    queso = Producto("queso", 2.8, "Lacteos")
    tienda.agregar_producto(leche)
    tienda.agregar_producto(queso)
    
def test_agrega_producto():
    tienda=Tienda()
    agregarProductos(tienda)
    assert len(tienda.inventario)==2
    
def test_busca_producto1():
    tienda = Tienda()
    agregarProductos(tienda)
    assert tienda.buscar_producto("queso")!=None
    
def test_busca_producto2():
    tienda = Tienda()
    agregarProductos(tienda)
    assert tienda.buscar_producto("leche")!=None
    
##El test falla a proposito
def test_busca_producto3():
    tienda = Tienda()
    agregarProductos(tienda)
    assert tienda.buscar_producto("obleas")==None
    
def test_elimina_producto1():
    tienda = Tienda()
    agregarProductos(tienda)
    assert tienda.eliminar_producto("leche")

##El test falla a proposito
def test_elimina_producto2():
    tienda = Tienda()
    agregarProductos(tienda)
    assert not tienda.eliminar_producto("zeta")
