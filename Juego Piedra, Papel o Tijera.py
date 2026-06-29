import random

def determinar_ganador(jugada_usuario, jugada_computadora, reglas_juego):
    if jugada_usuario == jugada_computadora:
        return "Empate"
    elif reglas_juego[jugada_usuario] == jugada_computadora:
        return "Usuario"
    else:
        return "Computadora"
def jugar_proyecto_final():
    puntos_usuario = 0
    puntos_computadora = 0  
    opciones = ("piedra", "papel", "tijera")
    reglas = {
        "piedra": "tijera",
        "papel": "piedra",
        "tijera": "papel"
    } 
    historial_partidas = []
    print("==================================================")
    print("¡BIENVENIDO AL JUEGO DE PIEDRA, PAPEL O TIJERA!")
    print("Este juego dura 3 rondas. !Buena suerte amigo¡")
    print("==================================================")
    for ronda in range(1, 4):
        print(f"\n--- RONDA {ronda} ---")
        usuario = input("Elije piedra, papel o tijera (o escribe 'salir'): ").lower()
        if usuario == "salir":
            print("¡Has decidido abandonar el juego!. Hasta pronto... :c")
            break
        if usuario not in opciones:
            print("Opción no valida. Perdiste esta ronda por error de escritura. :/")
            puntos_computadora +=  1
            historial_partidas.append("Invalido (Punto Computadora)")
            continue
        computadora = random.choice(opciones)
        print(f"La computadora eligió: {computadora}")
        resultado_ronda = determinar_ganador(usuario, computadora, reglas)
        if resultado_ronda == "Empate":
            print("¡Es un empate en esta ronda!")
            historial_partidas.append("Empate")
        elif resultado_ronda == "Usuario":
            print("¡Ganaste esta ronda! :)")
            puntos_usuario += 1
            historial_partidas.append("Ganó Usuario")
        else:
            print("La computadora ganó esta ronda.")
            puntos_computadora += 1
            historial_partidas.append("Ganó Computadora")
    print("\n==================================================")
    print("   FIN DEL JUEGO   ")
    print("==================================================")
    print(f"Puntaje Final -> Tú:{puntos_usuario} / Computadora: {puntos_computadora}")
    print(f"Historial Detallado: {historial_partidas}")
    print("--------------------------------------------------")
    if puntos_usuario > puntos_computadora:
        print("¡FELICIDADES! ERES EL GANADOR DEL JUEGO.")
    elif puntos_computadora > puntos_usuario:
        print("La computadora ganó el juego. >:/ ¡Sigue intentando!")
    else:
        print("El juego termino para tu buena suerte :D.")
jugar_proyecto_final()                                 