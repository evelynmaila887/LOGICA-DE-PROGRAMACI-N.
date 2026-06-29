# LOGICA-DE-PROGRAMACI-N.
PROYECTO INTEGRADOR.

JUEGO DEL PIEDRA, PAPEL O TIJERA.

Nombre: Evelyn Maila
Fecha: 28/06/2026.

Objetivo del sistema.
Desarrollar un simulador interactivo en Python del clásico juego "Piedra, Papel o Tijera" orientado a la consola. El sistema buscará aplicar de forma práctica los fundamentos de programación estructurada, lógica condicional y estructuras de datos dinámicas, permitiendo al usuario enfrentarse a una computadora bajo un entorno controlado de 3 rondas.

Descripción de Funcionalidades.
El sistema esta pensado para ser sencill, entretenido y muy ordenado. Al iniciar el programa te da la bienvenida y usa un ciclo automatico para controlar que la partida solo dure exactamente 3 rondas. n cada una de ellas, te permite escribir tu opción (piedra, papel o tijera); si te equivocas al escribir, el sistema lo detecta, te avisa que perdiste la ronda por error y continúa con la siguiente, aunque también te da la oportunidad de escribir 'salir' si quieres cerrar el juego antes de tiempo. Para decidir el ganador, la computadora elige su jugada al azar y el programa revisa rápidamente un diccionario con las reglas para saber quién venció a quién de forma limpia. Mientras juegas, el sistema va guardando las respuestas en una lista que sirve como memoria o historial. Al terminar las 3 rondas, el código suma los puntajes de ambos, te muestra el historial detallado, anuncia al campeón definitivo y, si terminan en un empate global, cierra con un mensaje muy divertido donde la computadora se muestra un poco envidiosa por no haberte podido ganar.




*DOCUMENTO DEL PROYECTO*

Introducción.
Este documento detalla el desarrollo de un simulador de un juego que todos conocemos, el cual es "PIEDRA PAPEL O TIJERA" programado en lenguaje de Python. El objetivo principal de este trabajo es integrar los conocimientos adquiridos en las clases, pasando de la teoría a la creación de un software. Se busca demostrar cómo la lógica de programación y el pensamiento estructurado permiten automatizar un juego interactivo, logrando que la computadora actúe como un oponente dinámico para el usuario.

Descrpción del problema.
Al iniciar en la programacíon lo más difícil es entender cómo aplicar las estructuras de datos y el control de flujos, ya que muchas veces los conceptos se quedan solo en teoría. Para este proyecto, el problema a resolver consistía en diseñar un juego que no solo automatizara las decisiones de la computadora, sino que también fuera capaz de seguir las reglas del juego de manera correcta y tratar de no cometer errores, además de verificar que el usuario no ingrese datos incorrectos y llevar un registro ordenado de los puntajes sin hacer que el código sea gigante o confuso. Este software resuelve este problema al centralizar las reglas en un sistema inteligente y seguro, garantizando así una mejor experiencia de juego y sin errores de ejecución.

Relación con los contenidos de la asignatura.
El diseño de este software esta basado en el cronograma y los temas estudiados. En primer lugar, se utilizaron variables y operadores matemáticos para crear y actualizar los marcadores de juego (Semana 3). El flujo general sigue un algoritmo ordenado que guía al usuario desde la bienvenida hasta los resultados finales (Semana 4). Para la toma de decisiones y la validación de lo que escribe el jugador,decidí agregar estructuras condicionales (Semana 5), las cuales funcionan dentro de un bucle "for" encargado de controlar que la partida dure solo tres rondas (Semana 6). Finalmente, los conceptos de la Semana 7 son el uso de una tupla para congelar las opciones válidas, un diccionario para evaluar instantáneamente al ganador de cada ronda, una lista que actúa como el historial del juego y funciones que ordenan el código.

Explicación del Software.
El sistema se construyó de forma que sea fácil de entender. Al empezar, el programa inicia un ciclo que se repetirá tres veces, donde en cada ronda solicita una opción al usuario. El código incluye un sistema de control que detecta si el jugador comete un error al escribir, dándole el punto a la computadora y saltando a la siguiente ronda con el alterador continue, o cerrando el programa con un break si se escribe la palabra 'salir'. Para que funcione, el programa envía las opciones a que sean comparadas con un diccionario de reglas; esta función determina el ganador de la ronda, actualiza el marcador y guarda la información en una lista de historial. Una vez completadas las rondas, analiza los resultados acumulados, muestra la lista con los detalles de cada partida y anuncia al ganador definitivo. 

Reflexión.
Desarrollar este proyecto permite comprender el verdadero impacto que tiene la tecnología y la creación de software en el mundo actual. Aunque se trata de un juego básico, la lógica utilizada para resolver este problema es la misma con la que se construyen sistemas y aplicaciones todos los días. Aprender a estructurar un código nos enseña a romper problemas complejos en partes pequeñas, lo que demuestra que la tecnología no solo sirve como entretenimiento, sino como una herramienta fundamental para optimizar procesos, desarrollar soluciones innovadoras y expandir nuestra capacidad de análisis crítico ante los retos del futuro.
