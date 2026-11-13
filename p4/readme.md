
# TeleTaxi


El objetivo de esta práctica se basa en crear un coche autónomo capaz de moverse mediante navegación global a través de una ciudad.


<img width="1034" height="443" alt="mapa_21x9_centrado" src="https://github.com/user-attachments/assets/d0f77cb9-5f26-4e34-b3d7-b57a237ae6a7" />


La idea principal es que sea capaz de llegar a el destino mediante el método de **Gradient Path Planning**.


Lo primero es cargar el mapa sobre el cual se tiene que mover el coche, este no se muestra hasta que no se seleccione un punto en específico, de esta forma  el programa espera y conseguimos que no malgaste muchos recursos mientras no hya nada, una vez que se merca ya se empieza a generar.

Para conseguir el mapa, he tenido que analizar las propiedades del mismo, viendo que se encuentra en una escala de grises y que prinicpalmente toma valor 0 a 255. 0 es obstáculo y 255 camino.

En mi caso he creado una función que se encarga de generarlo. Lo primero es generar una matriz vacía de dimensiones del mapa cargado, siendo una 400x400 y empiezan con costes sin poner, después se empieza desde la casilla objetivo con un peso 0 y se mira las casillas del alrededor con las direcciones N, S, E, W, NE, NW, SE y SW, cada uno con su respectivo coste.
Tras mirar las celdas vecinas y añadir su peso, nuestro algoritmo está implementado de forma BFS, Breadth-First Search, o en español, búsqueda con anchura. Se basa en ir mirando todas las casillas de un mismo nivel antes de pasar al anterior, en nuestro caso mira las casillas a distancia más cercana y tras mirar todas pasa a las siguientes más lejanas (de menos a más).
Está implementado con un heap, una cola que según vas metiendo va ordenando de menor a mayor, así conseguimos poder aplicar el BFS mejor sin tener que crear otra función auxiliar que reordene la cola constantemente sumando latencia, se consigue así optimizar recursos.


Cada vez que la onda llega a una celda vecina, calcula su coste como coste de la celda de la que viene + paso a esa celda + penalización por cercanía a la pared.
La onda se va expandiendo hasta completar el mapa y hay algunas celdas que se pueden llegar por muchos caminos, asi que si ese valor es menor que el que ya tenía guardada la celda, lo actualiza. Así, cada celda termina con el coste de la mejor ruta hasta el destino. 


Una vez que se tiene las celdas, se suma un peso extra cerca de las paredes, asignamos  a cada celda del mapa un coste extra según lo cerca que esté de una pared: para cada desplazamiento posible dentro de un cuadrado de radio 4 casillas, evitando así que no se pegue a las paredes el coche. Se calcula mediante K * (R + 1 - d), donde d es la distancia a la pared. Cuanto más pegada está la celda a un muro, mayor es la penalización. Esta se calcula una vez y se superpone con la anterior.

Para aumentar el peso, tuve el problema de que no era muy grande la diferencia, así que las que marco cerca las multiplico por una constante K para que crezcan. 

Una vez que está el mapa, se muestra y procede a crear el camino má corto desde el coche hasta el destino. Sigue la lógica de moverse por grandiente, es decir, se comprueban las 8 casillas alrededor del coche y se desplaza a la de menor coste, así sucesivamente hasta que llega a el objetivo. Con el mapa creado anteriormente, el coche es capaz de calcular constantemente su ruta y que casillas tiene que seguir para ir por el menor coste y así poder también visualizar nosotros su camino.




El coche para moverse, primero mira las celdas qeu tiene en el camino, mira como mucho las 5 primeras. Mira 5 en vez de 1 para que no tenga movimientos muy robóticos y pueda moverse de forma fluida, con más ignraría las esquinas y podría quedarse atascado en alguna.


Después se encarga de ver la distancia hasta el destino y calcula el ángulo entre su posiciń y destino con trigonometría. Se calcula de una forma similar que en la prácitca anterior, dependiendo del ángulo entre los puntos toma otro de salida  que hace que gire hacía el objetivo  para orientarse. De esta forma es capaz de girar en velocidad angular; para la velocidad lineal aplicamos como la práctica anterior, se toma el valor absoluto del ańgulo (evitar velocidades negativas que tiren hacia atrás) y se hace unitario, así el coche no empieza a frenar cuando se acerque , teniendo simpre una velocidad constante. Por último se le resta a 1  para que aumente cuando vaya en línea recta y no tanto cuando gire (aportando sentido y algo de realismo ala conducción), se le pone una velocidad mínima y se multiplica por una constante.

Así el coche es capaz de llegar a su destino.
