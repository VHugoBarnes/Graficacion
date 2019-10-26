# -*- coding: utf-8 -*-
# Programa por Brandon Esquivel y Cassandra González

import random
from time import sleep

print "Bienvenido al juego de  piedra, papel o tijera."
print ""
sleep(2)
print "Por defecto ganara el mejor de tres, pero lo puedes cambiar."
sleep(1)
print ""


# Funcion de la lógica del juego
def juego(intentos):
    x = 0
    jugador = 0
    pc = 0
    while str(x) != intentos:
        print "Piedra, papel o tijera?"
        opc = raw_input()
        opc = opc.lower()
        azar = random.choice(["piedra", "papel", "tijera"])
        if opc == azar:
            print "La computadora  tambien elijio", azar
            print ""
        elif azar == "tijera" and opc == "papel":
            x += 1
            pc += 1
            print "El PC saco", azar
            print "Tu", jugador, "PC", pc
            print ""
        elif azar == "tijera" and opc == "piedra":
            x += 1
            jugador += 1
            print "La computadora saco", azar
            print "Tu", jugador, "PC", pc
            print ""
        elif azar == "piedra" and opc == "tijera":
            x += 1
            pc += 1
            print "La computadora saco", azar
            print "Tu", jugador, "Computadora", pc
            print ""
        elif azar == "piedra" and opc == "papel":
            x += 1
            jugador += 1
            print "El PC saco", azar
            print "Tu", jugador, "PC", pc
            print ""
        elif azar == "papel" and opc == "tijera":
            x += 1
            jugador += 1
            print "La computadora saco", azar
            print "Tu", jugador, "Computadora", pc
            print ""
        elif azar == "papel" and opc == "piedra":
            x += 1
            pc += 1
            print "La computadora saco", azar
            print "Tu", jugador, "Computadora", pc
            print ""
        else:
            print "Opcion incorrecta, intentalo otra vez"

    print ""

    if pc > jugador:
        print "Gano la computadora", pc, "a", jugador
    elif pc == jugador:
        print "Empataron", jugador, "a", pc
    else:
        print "Ganaste", jugador, "a", pc

    print ""
    print "El juego termino"


def main():
    print "Escribe 1 para jugar al mejor de tres."
    print "Escribe 2 para cambiar la modalidad del juego."

    opcion = input()

    if opcion == 1:
        juego("3")
        print ""
        restart = raw_input("Quieres jugar de nuevo?(s/n): ")
        restart = restart.lower()
        if restart == "s":
            print ""
            main()
    else:
        intentos = raw_input("Introduce el numero de partidas: ")
        juego(intentos)
        print ""
        restart = raw_input("Quieres jugar de nuevo?(s/n): ")
        restart = restart.lower()
        if restart == "s":
            print ""
            main()
        else:
            print "Fin"


main()