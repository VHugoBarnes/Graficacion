# -*- coding: utf-8 -*-
# Programa de Alexis y Hector
import os, sys
import random


global cartas
cartas=[2,3,4,5,6,7,8,9,10,'AS','J','Q','K']
suma1=0
suma2 = 0
global jugador1
jugador1 = []
global jugador2
jugador2 = []

print '\n                      ----Bienvenido a Black Jack----\n'



op=0
while op!=6:

    op = input('Si desea una carta preciona 1, si desea parar preciona 6:')
    if op == 1:
        suma1 = 0
        valorJ = 0
        valorK = 0
        valorQ = 0
        valorAs = 0
        print '\n                          Turno de jugador 1'

        eleccion = random.choice(cartas)
        print 'Carta-----', eleccion
        if eleccion == 'AS':
            valorAS = int(input('Que valor desea darle a el AS 1 o 10?:'))
            jugador1.append(valorAS)
        elif eleccion == 'J':
            jugador1.append(10)
        elif eleccion == 'Q':
            jugador1.append(10)
        elif eleccion == 'K':
            jugador1.append(10)

        else:
            jugador1.append(eleccion)
        print '\nCartas encontradas----- ',jugador1, ('\n')

        for i in jugador1:
            suma1 = suma1 + i

        print 'Suma de puntos....', suma1

        if suma1 > 21:
            print '\nLo siento mucho pero usted ha perdido'
            print '\nEmpezara el turno del otro participante '
            break
            clear()
        elif suma1 == 21:
            print 'Muchas felicidades ha obtenido los 21 puntos '
            break

print'\n-----*-----*-----*-----*----*-----*-----*-----*-----*----*-----*-----*-----*-----*----*'
print'-----*-----*-----*-----*----*-----*-----*-----*-----*----*-----*-----*-----*-----*----*\n'
print '\n                          Turno de jugador 2'

oper = 0
while oper != 9:

    oper = input('Si desea una carta 1preciona 1, si desea parar preciona 9:')
    if oper == 1:
        suma2 = 0
        valorJ = 0
        valorK = 0
        valorQ = 0
        valorAs = 0

        print '\n                          Turno de jugador 2'

        eleccion = random.choice(cartas)
        print 'Carta-----', eleccion
        if eleccion == 'AS':
            valorAS = int(input('Que valor desea darle a el AS 1 o 10?:'))
            jugador2.append(valorAS)
        elif eleccion == 'J':
            jugador2.append(10)
        elif eleccion == 'Q':
            jugador2.append(10)
        elif eleccion == 'K':
            jugador2.append(10)

        else:
            jugador2.append(eleccion)
        print '\nCartas encontradas ',jugador2, ('\n')

        for i in jugador2:
            suma2 = suma2 + i

        print 'Suma de puntos....', suma2

        if suma2 > 21:
            print 'Lo siento mucho pero usted ha perdido'
            break
        elif suma1 == 21:
            print 'Muchas felicidades ha obtenido los 21 puntos '
            break




print'\n-----*-----*-----*-----*----*-----*-----*-----*-----*----*-----*-----*-----*-----*----*'
print'-----*-----*-----*-----*----*-----*-----*-----*-----*----*-----*-----*-----*-----*----*\n'



print '\nSuma de puntos del jugador 1....', suma1

print '\nSuma de puntos del jugador 2....', suma2

if suma1>21 and suma2>21:
    print '\nLos 2 jugadores perdieron'

if suma1==21 and suma2!=21:
    print '\nEl jugador 1 es quien gana la partida'

if suma2==21 and suma1!=21:
    print '\nEl jugador 2 es quien gana la partida'

if suma1==21 and suma2==21:
    print '\nEmpate entre los jugadores :O'

if suma1<21 and suma2>21:
    print '\nEl jugador 1 es quien gana la partida'

if suma1>21 and suma2<21:
    print '\nEl jugador 2 es quien gana la partida'

if suma1<21 and suma2<21:
    if suma1 > suma2:
        print '\nEl jugador 1 es quien gana la partida'

if suma1<21 and suma2<21:
    if suma2>suma1:
        print '\nEl jugador 2 es quien gana la partida'