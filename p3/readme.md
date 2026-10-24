# Robot esquiva obstáculos.

Esta práctica consiste en implementar un algortimo capaz de hacer que el coche pueda esquivar obstáculos y ser capaz de navegar por el mapa utilizando localización local.

<img width="712" height="400" alt="imagen_horizontal_400" src="https://github.com/user-attachments/assets/fa079dac-f0e2-4221-b96d-f788cd6232c1" />


Para ello utilizamos un sistemas de vectores con el cual intentamos pasar por distintos puntos de ruta (chekpoints) mientras esquivamos coches que se encuentran en el camino.
La lógica general es crear un vector atractivo a el primer checkpoint, otro repulsivo de los objetos y el resultante que es combinación de los dos anteriores.


Lo primero es marcar el primer objetivo a seguir con el nextTarget y obtenemos los datos de posiciones tanto del objetivo como del coche y su ángulo. Una vez qye tenemos todos 
los datos necesarios, lo que hacemos es llamar a l función "absolute2relative", conseguimos transformar la posición y así poder calcular la posición relativa del coche al objetivo (dividida en x e y).

Antes de empezar a calcular fuerzas, comrpobamos que no estamos en el checkpoint, para ello hacemos un umbral de < 1 con el que **"engordamos"** el punto y así conseguimos saber si hemos conseguido ese objetivo o no.
<p>


Ahora sí ya calculamos una fuerza **atractiva.** Lo primero que realizamos es normalizar la posición relativa para así poder tenerla deifinida en un rango entre 0 y 1, al estar dividiendo constantemente entre la distancia, esta siempre se va a mantener constante y así evitamos que al haber poca distancia hasta el checkpoint se frene o desaparezca la fuerza atractiva.

<p>
 

Para la fuerza **repulsiva** utilizamos el laser del coche, este mide todos los ángulos posibles entre 0º y 180º que abarcan la parte frontal (0 es la izquierda, 90 recto y 180 derecha).
Nos interesa los valores que sean suficientemente cercanos, así que ponemos mínimo de cercanía, si superan ese mínimo lo dividimos entre si son rangos laterales (enfocado a las paredes para evitar oscilaciones) y rangos frontales.
Como el vector crece en función de la distancia, si este se acerca tiene que ser mayor, es **inversamente proporcional** a la distancia.

Si es frontal, 1/distancia; si es lateral, 1/distancia².


Tenemos que tener en cuenta que el eje está desplazado 90 grados, así que el ángulo del laser le restamos 90.

Para la repulsiva multiplicamos esa distancia invertida por el ángulo (con coseno y seno para x e y), así la tenemos vectorialmente. La repulsiva la vamos acumulando para tener la de todos los láseres y así tenemos una repulsiva que intente repeler a todos los objetos.

Para terminar, la repulsiva la normalizamos igual que la atractiva, esta vez entre el número de láseres totales y así tenerla entre 0 y 1.


En la **resultante** lo que hacemos es la fuerza atractiva menos la repulsiva, las dos multiplicadas por un constante para cada uno, ajustada para poder esquivar los objetos y recorrer el circuito.
Esta fuerza resultante va a ir cambiando en cada iteración del bucle y así puede corregir el movimiento.


Una vez que sabemos hacia donde, nos queda transformarlo en instrucciones para el coche de setV y setW.
Calculamos así el ángulo, dependiendo de las componentes del resultante (su distancia en x e y).

Para ello utilizamos el arcotangente y en función de si es negativo, positivo o nulo (en la arcotangente se divide entre x y no se puede dividir entre 0) sacamos un ángulo.
Si es negativo lo que hacemos es sumar o restar pi (180º) y así poder llevarlo a alguno de los cuadrantes que observa el coche.

La velocidad angular multiplica este ángulo por una constante para que así pueda girar con cierta velocidad.
La velocidad lineal lo que hacemos es coger el módulo de este ángulo y normalizarlo para estar entere 0 y 1 (dividimos por pi). Con esto tenemos un ángulo que 0º es  0 (recto) y 180º es 1 (atrás), así que le damos la vuelta restandole ese valor a 1. Por último multiplicamos por una constante. Para asegurarnos de que va a tener una velocidad mínima lo que hacesmo es coger el máximo entre este número calculado y 0.5, así siempre habrá un mínimo de 0.5.


Vídeo de ejemplo completando el circuito:

