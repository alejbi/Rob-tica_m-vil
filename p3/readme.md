# Robot esquiva obstáculos.

Esta práctica consiste en implementar un algortimo capaz de hacer que el coche pueda esquivar obstáculos y ser capaz de navegar por el mapa utilizando localización local.

Para ello utilizamos un sistemas de vectores con el cual intentamos pasar por distintos puntos de ruta (chekpoints) mientras esquivamos coches que se encuentran en el camino.
La lógica general es crear un vector atractivo a el primer checkpoint, otro repulsivo de los objetos y el resultante que es combinación de los dos anteriores.


Lo primero es marcar el primer objetivo a seguir con el nextTarget y obtenemos los datos de posiciones tanto del objetivo como del coche y su ángulo. Una vez qye tenemos todos 
los datos necesarios, lo que hacemos es llamar a l función "absolute2relative", conseguimos transformar la posición y así poder calcular la posición relativa del coche al objetivo (dividida en x e y).

Antes de empezar a calcular fuerzas, comrpobamos que no estamos en el checkpoint, para ello hacemos un umbral de < 1 con el que "engordamos" el punto y así conseguimos saber si hemos conseguido ese objetivo o no.
<p>

</p>
Ahora sí ya calculamos una fuerza atractiva. LO primero que realizamos es normalizar la posición relativa para así poder tenerla deifinida en un rango entre 0 y 1, al estar dividiendo constantemente entre la distancia, esta siempre se va a mantener constante y así evitamos que al haber poca distancia hasta el checkpoint se frene o desaparece la fuerza atractiva.

