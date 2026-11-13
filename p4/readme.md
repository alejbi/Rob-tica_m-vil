
# TeleTaxi


El objetivo de esta práctica se basa en crear un coche autónomo capaz de moverse mediante navegación global a través de una ciudad.


<img width="1034" height="443" alt="mapa_21x9_centrado" src="https://github.com/user-attachments/assets/d0f77cb9-5f26-4e34-b3d7-b57a237ae6a7" />


La idea principal es que sea capaz de llegar a el destino mediante el método de **Gradient Path Planning**.


Lo primero es cargar el mapa sobre el cual se tiene que mover el coche, este no se muestra hasta que no se seleccione un punto en específico, de esta forma  el programa espera y conseguimos que no malgaste muchos recursos mientras no hya nada, una vez que se merca ya se empieza a generar.

En mi caso he creado una función que se encarga de generarlo. Lo primero es generar una matriz vacía de dimensiones del mapa cargado, siendo una 400x400 y empiezan con costes sin poner, después se empieza desde la casilla objetivo con un peso 0 y se mira las casillas del alrededor con las direcciones N, S, E, W, NE, NW, SE y SW, cada uno con su respectivo coste.
Tras mirar las celdas vecinas y añadir su peso, nuestro algoritmo está implementado de forma BFS, Breadth-First Search, o en español, búsqueda con anchura. Se basa en ir mirando todas las casillas de un mismo nivel antes de pasar al anterior, en nuestro caso mira las casillas a distancia más cercana y tras mirar todas pasa a las siguientes más lejanas (de menos a más).
Está implementado con un heap, una cola que según vas metiendo va ordenando de menor a mayor, así conseguimos poder aplicar el BFS mejor sin tener que crear otra función auxiliar que reordene la cola constantemente sumando latencia, se consigue así optimizar recursos.
Cada vez que la onda llega a una celda vecina, calcula su coste como coste de la celda de la que viene + paso a esa celda + penalización por cercanía a la pared.
La onda se va expandiendo hasta completar el mapa y hay algunas celdas que se pueden llegar por muchos caminos, asi que si ese valor es menor que el que ya tenía guardada la celda, lo actualiza. Así, cada celda termina con el coste de la mejor ruta hasta el destino. 


UNa vez que se tiene las celdas, se suma un peso extra cerca de las paredes, asignamos  a cada celda del mapa un coste extra según lo cerca que esté de una pared: para cada desplazamiento posible dentro de un cuadrado de radio 4, evitando así que no se pegue a las paredes el coche. Se calcula mediante K * (R + 1 - d), donde d es la distancia a la pared. Cuanto más pegada está la celda a un muro, mayor es la penalización. Esta se calcula una vez y se superpone con la anterior.



Una vez que está el mapa, se muestra y procede a crear el camino má corto desde el coche hasta el destino. Sigue la lógica de moverse por grandiente, es decir, se comprueban las 8 casillas alrededor del coche y se desplaza a la de menor coste, así sucesivamente hasta que llega a el objetivo. Con el mapa creado anteriormente, el coche es capaz de calcular constantemente su ruta y que casillas tiene que seguir para ir por el menor coste y así poder también visualizar nosotros su camino.
