# Robotica_movil


# Practica 1: Aspiradora básica


El objetivo de esta primera práctica consiste en implementar una pqueña aspiradora (coloquialmente conocida como "rumba") a la casa.

Para ello hemos utilizado unibotics y el fichero "copy.py" que viene dado de forma predeterminada.

Lo primero  son los import, entre los que incluimos nosotros algunos como math, random o time a parte de los que vienen de WebGUI,...

Lo que hemos hecho es implementar una máquina de estados, en los que podemos transitar como **ADELANTE**, **REOTRCEDER** o **GORAR**.

Para poder saber en qué estado estamos, utilizamos una variable que va cambiando dependiendo de la situación.

Dentro del bucle while, utilizamos la frecuencia del tick predeterminada 50Hz ya que para este caso de la aspiradora no es necesario mucha más precisión ni velocidad.

Obtenemos los datos del laser, verificamos que sean válidos y nos quedamos con el de ángulo de valor 90, que se refiere a la dirección en línea recta. En ese instante obtenemos el tiempo.

En el caso de se reduzca la distancia a menos de 0.6, transita al estado RETROCEDER y guarda el tiempo,una vez que ya se encuentra en RETROCEDER, lo que hace es calcular la diferencia de tiempos y mira si es menor a 1 segundo. Con esto coseguimos que retroceda 1s.

Después lo que hace es cambiar el valor de grados: primero selecciona un numero entre -1 y 1, ya que los negativos son a la izquierda y los positivos a la derecha; y después lo multiplica entre otro valor al azar entre 0.5 y 1.5, con esto consigue que gire, el 0.5 para que no sea un giro demasiado pequeño, y el 1.5 para que le permita girar sin deslizarse el robot.

Transita hasta el estado GIRAR.


Allí simplemente gira sobre si mismo y lo hace durante 1.5s. En ese tiempo verifica que no haya un muro y así poder volver a ir hacia adelante.


Los estados están anunciados a donde transitan.


Como quedaría la casa después de dejarle 10 minutos limpiando

<img width="716" height="835" alt="Screenshot From 2026-10-01 17-09-17" src="https://github.com/user-attachments/assets/371a5d34-7061-4552-9fbf-6bbbf2e7f02f" />

Video de ejecución:


[Screencast From 2026-10-01 17-45-53.webm](https://github.com/user-attachments/assets/1429f9f7-8ed4-49e8-bf71-f7d785f7c6d5)

