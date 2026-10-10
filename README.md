# Robotica_movil


# Practica 1: Aspiradora básica


El objetivo de esta primera práctica consiste en implementar una pqueña aspiradora (coloquialmente conocida como "rumba") a la casa.

Para ello hemos utilizado unibotics y el fichero "copy.py" que viene dado de forma predeterminada.

Lo primero  son los import, entre los que incluimos nosotros algunos como math, random o time a parte de los que vienen de WebGUI,...

Lo que hemos hecho es implementar una máquina de estados, en los que podemos transitar como **ADELANTE**, **REOTRCEDER** o **GIRAR**.

Para poder saber en qué estado estamos, utilizamos una variable que va cambiando dependiendo de la situación.

Dentro del bucle while, utilizamos la frecuencia del tick predeterminada 50Hz ya que para este caso de la aspiradora no es necesario mucha más precisión ni velocidad.

Obtenemos los datos del laser, verificamos que sean válidos y nos quedamos con el de ángulo de valor 90, que se refiere a la dirección en línea recta. En ese instante obtenemos el tiempo.

En el caso de se reduzca la distancia a menos de 0.6, transita al estado RETROCEDER y guarda el tiempo,una vez que ya se encuentra en RETROCEDER, lo que hace es calcular la diferencia de tiempos y mira si es menor a 1 segundo. Con esto coseguimos que retroceda 1s.

Después lo que hace es cambiar el valor de grados: primero selecciona un numero entre -1 y 1, ya que los negativos son a la izquierda y los positivos a la derecha; y después lo multiplica entre otro valor al azar entre 0.5 y 1.5, con esto consigue que gire, el 0.5 para que no sea un giro demasiado pequeño, y el 1.5 para que le permita girar sin deslizarse el robot.

Transita hasta el estado GIRAR.


Allí simplemente gira sobre si mismo y lo hace durante 1.5s. En ese tiempo verifica que no haya un muro y así poder volver a ir hacia adelante.


Los estados están anunciados a donde transitan.


Como quedaría la casa después de dejarle 10 minutos limpiando:

<img width="716" height="835" alt="Screenshot From 2026-10-01 17-09-17" src="https://github.com/user-attachments/assets/371a5d34-7061-4552-9fbf-6bbbf2e7f02f" />

Video de ejecución:


[Screencast From 2026-10-01 17-45-53.webm](https://github.com/user-attachments/assets/1429f9f7-8ed4-49e8-bf71-f7d785f7c6d5)





# práctica 2: Coche F1


El funcionamiento de esta práctica consiste en recrear el funcionamiento de un coche autonónomo.

El objetivo es implementar un controlador de tipo P, PD o PID que sea capaz de realizar los circuitos en el menor tiempo posible, simulando el control de una persona normal.

La clabe del coche es seguir la línea central roja, de esta forma el coche funciona como un **sigue-lineas** y completa el circuito.


Lo primero es ser capaz de definir qué es lo que busca, con un filtro de color hsv extraemos solo el color rojo de la imagen. Definimos el rango en el que se encuentra el color rojo entre todos los posibles, el rango completo es de 0 a 255 y el rojo se encuentra de 0 10 y de 170 a 179. El primer rango de 0 a 10 es el que usamos, es el rango donde mejor se puede leer el color rojo y el mapa al no tener texturas de sombras no va a estar cambiando la tonalidad del rojo, por lo que siempre va a ser igual y por tanto no hace falta analizar los dos. Conseguimos así simplificar el código.

Una vez encontrado el color rojo lo que hacemos es transformalo en blanco para poder nosotros veerlo mejor y aplicamos las cotas.

Una vez que ya tenemos el dato refinado de la cámara sobre el color rojo nos quedamos con una franja horizontal solo. La imagen tiene un rango de 0 a 480, tenemos que buscar una franja que analizar. La linea está en el suelo por lo que tiene que ser desde el horizonte (el centro del campo de visión) hacia abajo. A la hora de decidir que medir primero puse la linea en 240, el límite, pero media valores demasiado lejanos y que alteraban demasiado el coche, por eso cojemos unas líneas más abajo, la 280.

Una vez que ya tenemos que analizar, verificamos que haya valores de linea para saber si observa la linea o no, si la ve. Lo que hace es ver donde se encuentra el rojo y ver la distancia hasta el centro.

Dependiendo de los valores que da se encarga de girar hacia algún lado o ir recto. 
Si va recto se pone a acelerar hasta la velocidad máxima que alcanza el coche. (Simulando que tiene un límite de velocidad para hacerlo más realista como si tuviera una velocidad punta).


