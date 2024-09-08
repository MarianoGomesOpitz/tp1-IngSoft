# tp1-IngSoft
1) Unicamente puede testearse de forma individual la funcion agregar_producto. El resto son pruebas de integracion

2) Sí, se podría escribir primero las pruebas antes que el código. El proceso consistirá en:
1- Considerar los requisitos fundamentales y las posibles salidas del sistema.
2- Escribir los tests que aseguren y prueben que el programa cumpla con dichos requisitos, poniendo el foco en qué entradas o condiciones producen las salidas esperadas.
3- Escribir el código según nuestras consideraciones, solo lo fundamental para las pruebas, sin agregar funcionalidades extra que no estén consideradas.
4- Realizar los tests para comprobar que el código funcione como debería hacerlo. Estos tests podrían fallar o pasar, según cómo estén definidos.
5- Ajustar el código iterativamente: si hay fallas, se ajusta el código y se vuelve a probar, así sucesivamente hasta que cumpla con todos los requisitos.

3) En lo que va del tp, se puede identificar que los drivers son aquellos modulos que empiezan por "test_", que sirven para probar los módulos. En cambio, la aparición de resguardos se da en este ejercicio con la utilización de mocks, para simular el valor de retorno de un módulo.
Un mock es un objeto simulado que reemplaza un componente o dependencia real del código durante una prueba. Los mocks se utilizan para aislar la unidad de código que se está probando, asegurando que las pruebas no dependan de otros componentes externos o de comportamientos impredecibles. Otros nombres por los que se le conoce a los mocks son resguardos, stubs, spy, fake, patch.

4) La ventaja que se ve en la utilizacion de fixtures es el poder inicializar de manera más rápida y sencilla un objeto, lo que facilita y agiliza el proceso de prueba.
En este caso dado, el enfoque que estaríamos usando sería el de caja negra, ya que de la manera en que lo usamos solo tenemos en cuenta los datos de entrada y las salidas que estos producen, sin interesarnos en la implementación interna. Cabe aclarar que los fixtures pueden tener un enfoque de caja negra o caja blanca, dependiendo de la prueba.
El setup es el proceso de preparación que se realiza antes de ejecutar una prueba. Incluye todas las tareas necesarias para poner el sistema o la unidad de código en un estado adecuado para la prueba. Asegura que cada prueba comience con un entorno conocido, limpio y predecible, donde todos los componentes necesarios estén inicializados correctamente. Por ejemplo: Inicializar objetos o instancias de clases, establecer conexiones a bases de datos o servicios externos, preparar datos de prueba, como insertar registros en una base de datos, etc.
El teardown es el proceso de limpieza que se realiza después de que una prueba ha terminado. Incluye todas las tareas necesarias para restaurar el sistema o el entorno a un estado neutral o revertir los cambios hechos durante el setup. Asegura que el entorno de prueba vuelva a un estado limpio, sin interferencias, para que las pruebas posteriores no se vean afectadas por los cambios realizados en las pruebas anteriores. Por ejemplo:
- Cerrar conexiones a bases de datos o servicios.
- Eliminar o revertir datos insertados durante la prueba.
- Restablecer configuraciones de sistema o limpiar archivos temporales.
- Liberar recursos utilizados durante la prueba.

5) Una situación de desarrollo en la que las pruebas sean de integración ascendente es uno en el que se desarrolla cada módulo de nivel inferior y al tenerlo probado hasta un punto satisfactorio, se prosigue con un módulo de nivel superior que utiliza ese módulo inferior.
Un ejemplo puede ser el de este mismo TP. Primero se desarrolla el objeto Producto con todos las funcionalidades que le corresponden, se las prueba de manera exhaustiva para corrobar que funcione correctamente, y encontrar y solucionar posibles errores de funcionamiento. Luego se continua con la Tienda, que utiliza al Producto y a sus funciones para sí mismas. Se realizan pruebas que verifiquen su funcionamiento, y al ya saber que el Producto funciona correctamente, los posibles errores que pueden aparecer son del funcionamiento de la Tienda, o de implementación del Producto en la Tienda. Para el final realizar la función de calcular la compra que utiliza todas las funciones de la Tienda.
