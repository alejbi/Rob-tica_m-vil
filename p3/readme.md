# Robot esquiva obstáculos.

Esta práctica consiste en implementar un algortimo capaz de hacer que el coche pueda esquivar obstáculos y ser capaz de navegar por el mapa utilizando localización local.

Para ello utilizamos un sistemas de vectores con el cual intentamos pasar por distintos puntos de ruta (chekpoints) mientras esquivamos coches que se encuentran en el camino.
La lógica general es crear un vector atractivo a el primer checkpoint, otro repulsivo de los objetos y el resultante que es combinación de los dos anteriores.


Lo primero es marcar el primer objetivo a seguir con el nextTarget y obtenemos los datos de posiciones tanto del objetivo como del coche y su ángulo. Una vez qye tenemos todos los datos necesarios, lo que hacemos es llamr  
