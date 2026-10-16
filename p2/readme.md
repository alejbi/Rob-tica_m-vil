# Práctica 2: Coche F1


El funcionamiento de esta práctica consiste en recrear el funcionamiento de un coche autonónomo.

El objetivo es implementar un controlador de tipo P, PD o PID que sea capaz de realizar los circuitos en el menor tiempo posible, **simulando el control de una persona normal**.

La clabe del coche es seguir la línea central roja, de esta forma el coche funciona como un **sigue-lineas** y completa el circuito.


Lo primero es ser capaz de definir qué es lo que busca, con un filtro de color hsv extraemos solo el color rojo de la imagen. Definimos el rango en el que se encuentra el color rojo entre todos los posibles, el rango completo es de 0 a 255 y el rojo se encuentra de 0 10 y de 170 a 179. El primer rango de 0 a 10 es el que usamos, es el rango donde mejor se puede leer el color rojo y el mapa al no tener texturas de sombras no va a estar cambiando la tonalidad del rojo, por lo que siempre va a ser igual y por tanto no hace falta analizar los dos. Conseguimos así simplificar el código.

Una vez encontrado el color rojo lo que hacemos es transformalo en blanco para poder nosotros veerlo mejor y aplicamos las cotas.

Una vez que ya tenemos el dato refinado de la cámara sobre el color rojo nos quedamos con una franja horizontal solo. La imagen tiene un rango de 0 a 480, tenemos que buscar una franja que analizar. La linea está en el suelo por lo que tiene que ser desde el horizonte (el centro del campo de visión) hacia abajo. A la hora de decidir que medir primero puse la linea en 240, el límite, pero media valores demasiado lejanos y que alteraban demasiado el coche, por eso cojemos unas líneas más abajo, la 280.

Una vez que ya tenemos que analizar, verificamos que haya valores de linea para saber si observa la linea o no, si la ve. Lo que hace es ver donde se encuentra el rojo y ver la distancia hasta el centro.

Dependiendo de los valores que da se encarga de girar hacia algún lado o ir recto. 
Si va recto se pone a acelerar hasta la velocidad máxima que alcanza el coche. (Simulando que tiene un límite de velocidad para hacerlo más **realista** como si tuviera una velocidad punta).

Cuando se encuentra en los  casos de girar reduce su velocidad lineal y empieza a girar (simluando un piloto que frena para poder tomar una curva).

Tiene implementado un controlador P para la lineal y otro para la angular. Lo que hace es multiplicar el error por una constante PD y (independiente para cada velocidad) por el error y sumarlo a la velocidad anterior que tenía, después utilizamos las funciones que hemos creado para hacer que no aumente ni reduzca mucho la velocidad (una velocidad mínima de lineal donde es seguro poder girar siempre y una velocidad angular de tope máximo para que no derrape y tenga sentido el giro).

Una vez verificada la velocidad con los límites ya la publica.

Con esto también conseguimos que **no oscile** el coche.


En el caso de qe no vea la linea tiene una función donde reduce la velocidad lineal hasta marcha atrás mientras gira, así puede buscar otra vez la línea para retomarla.

En el caso de Ackermann también es capaz de completar también todos los circuitos.


Video de vuelta en circuito simple:

[Screencast From 2026-10-13 16-34-02.webm](https://github.com/user-attachments/assets/f8e27dab-b33e-4e22-9829-cabcd74eadd9)




Videos con demostraciones en otras pistas de partes complicadas o que han dado problemas en el desarollo y ahora el coche es capaz de recorrer:

Incuye también los circuitos que tienen pianos de color rojo, demostrando que es capaz de correr en cualquier circuito


[Screencast From 2026-10-13 16-38-04.webm](https://github.com/user-attachments/assets/652e53a7-50a4-47cc-80d8-ad6b11d3cdae)

[Screencast From 2026-10-13 16-39-48.webm](https://github.com/user-attachments/assets/234d5085-72a8-4e1f-b731-7ba3cd888f9e)

[Screencast From 2026-10-13 16-49-40.webm](https://github.com/user-attachments/assets/eb33006c-71a0-4a9a-9645-a91a9c344348)

[Screencast From 2026-10-13 16-46-05.webm](https://github.com/user-attachments/assets/51a6f3c5-b0fd-4a43-8996-51d3841867e4)

[Screencast From 2026-10-13 16-45-01.webm](https://github.com/user-attachments/assets/02a898dc-5b49-46d1-a947-23e445184409)


Video de como evoluciona la velocidad angular y lineal a la hora de hacer curvas, con esto vemos como responde el coche de forma fluida y cercana a como sería pilotarlo de forma real, con su reducción de velocidad en curvas, su velocidad punta en 6,...

[Screencast From 2026-10-13 16-40-41.webm](https://github.com/user-attachments/assets/972252ac-bff9-4fb6-8059-bafc14ba70d4)




