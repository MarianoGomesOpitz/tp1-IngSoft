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
    

## La ventaja que se ve en la utilizacion de fixtures es el poder inicializar de manera más rápida y sencilla un objeto,
## lo que facilita y agiliza el proceso de prueba.
## La utilización de fixtures implica un enfoque de testeo aislado y controlado, permitiendo así que cada prueba se ejecute
## en un entorno repetible y predecible, lo que resulta en la fiabilidad y consistencia de los resultados.
## Al hablar de pruebas aisladas y controladas, nos referimos a pruebas de unidad, ya que se aisla el módulo a probar,
## sin especificar la relación del mismo con los otros.

## El setup es el proceso de preparación que se realiza antes de ejecutar una prueba. Incluye todas las tareas necesarias 
## para poner el sistema o la unidad de código en un estado adecuado para la prueba.
## Asegura que cada prueba comience con un entorno conocido, limpio y predecible, donde todos los componentes 
## necesarios estén inicializados correctamente.
## Por ejemplo: Inicializar objetos o instancias de clases, establecer conexiones a bases de datos o servicios externos,
## preparar datos de prueba, como insertar registros en una base de datos, etc.

## El teardown es el proceso de limpieza que se realiza después de que una prueba ha terminado. Incluye todas las tareas 
## necesarias para restaurar el sistema o el entorno a un estado neutral o revertir los cambios hechos durante el setup.
## Asegura que el entorno de prueba vuelva a un estado limpio, sin interferencias, para que las pruebas posteriores no 
## se vean afectadas por los cambios realizados en las pruebas anteriores.
## Por ejemplo: Cerrar conexiones a bases de datos o servicios.
## Eliminar o revertir datos insertados durante la prueba.
## Restablecer configuraciones de sistema o limpiar archivos temporales.
## Liberar recursos utilizados durante la prueba.