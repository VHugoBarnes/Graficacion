# -*- coding: utf-8 -*-
# Programa por Cynthia Barron y Alfredo Santos
import random
import textwrap
import time
global numeros
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
global palabras
palabras = ['edita', 'igual', 'habil', 'abajo', 'subir', 'programar', 'codigo', 'libreria', 'python',
                    'pycharm', 'graficacion', 'editor ', 'fuente', 'c', 'java',
                    'javascript', 'arreglo', 'bucle', 'for', 'while', 'random',
                    'choice', 'puntoycoma', 'llaves', 'main', 'variable',
                    'operacion', 'alineado', 'geometria fractal', 'formato', 'almacenamiento',
                    'hardware', 'software']



#funciones

def AdivinaElNumero():
    ancho_linea = 72
    linea_punteada = ancho_linea * '.'

    print(linea_punteada)
    volver_ajugar = 1

    print("\033[1m" + "Juego de adivina el numero" + "\033[0m")
    msg = ("Bienvenido al juego de adivina el numero."
           "El juego de adivina el numero, es un juego con el cual debemos adivinar el numero que piensa el otro jugador. En este caso la computadora es el que piensa el numero "
           "Crees que eres lo suficientemente bueno en adivinar, bueno pues juguemos, pero antes te dare las reglas, tienes solo 3 intentos, como en el tradicional, cada que te equivoques al ingresar un numero estas a una vida menos de perder, el numero es elegido aleatoriamente en un intervalo del 1 al 10, asi que no esperes adivinar tan facil, pero si eres bueno sera pan comido, y para no ser tan malo, cuando ingreses tu primer numero te dire si estas muy bajo o muy alto del numero en el que estoy pensando, SUERTE")
    print(textwrap.fill(msg, width=ancho_linea))
    print(linea_punteada)
    miNombre = raw_input('Escribe tu nombre:  ')
    while volver_ajugar == 1:
        numerosIntentos = 0  # El numero de veces que el jugador a intentado adivinar
        numero = random.choice(numeros)  # Para elegir un elemento aleatorio de una lista o arreglo

        print ('\n Bienvenid@, ' + miNombre + '. Estoy pensado en un numero del 1 y 10 ')

        while numerosIntentos < 3:
            print("\n Adivina en que numero estoy pensando: ")
            adivina = input()
            adivina = int(adivina)

            numerosIntentos = numerosIntentos + 1

            if adivina < numero:
                print ("Tu intento es demasiado bajo ")

            elif adivina > numero:
                print('Tu intento es demasiado alto')

            elif adivina == numero:
                break

        if adivina == numero:
            numerosIntentos = str(numerosIntentos)
            print('Buen trabajo' + miNombre + '.   Has adivinado mi numero en ' + numerosIntentos + '  intentos')

        if adivina != numero:
            numero = str(numero)
            print ('\n Se han terminado tus intentos. Perdiste !!! El numero que estaba pensando era ' + numero)

        print(linea_punteada)
        volver_ajugar = input("¿Quieres jugar de nuevo? Si(1)/No(0):")
        print(linea_punteada)





def Ahorcado():
    if __name__ == '__main__':
        volver_ajugar = 1
        ancho_linea = 72
        linea_punteada = ancho_linea * '.'
        print(linea_punteada)
        print("\033[1m" + "Juego del ahorcado" + "\033[0m")
        msg = ("Bienvenido al juego del ahorcado."
               "El juego del ahorcado, anteriormente se jugaba a lapiz y papel. "
               "Crees que eres lo suficientemente bueno en adivinar y usar estrategias para esto, bueno pues juguemos, pero antes te dare las reglas, tienes solo 5 intentos, como en el tradicional, cada que te equivoques al ingresar una letra estas a una vida menos de perder, las palabras son elegidas aleatoriamente, asi que no esperes adivinar tan facil, pero si eres bueno sera pan comido, y para no ser tan malo, recuerda que no hay palabras sin las vocales ;D , SUERTE")
        print(textwrap.fill(msg, width=ancho_linea))
        print(linea_punteada)
        nombre = raw_input("¿Como te llamas? ")
        while volver_ajugar == 1:
            print "Hola, ", nombre, ". Es hora de jugar al ahorcado."
            print
            time.sleep(1)
            print "Comienza a adivinar "
            time.sleep(0.5)

            palabra = random.choice(palabras)
            tupalabra = ''
            vida = 5
            while vida > 0:
                fallas = 0
                for letra in palabra:
                    if letra in tupalabra:
                        print letra,
                    else:
                        print "_",
                        fallas += 1
                if fallas == 0:
                    print("Felicidades, ganaste.")
                    break
                tuletra = raw_input("Introduce una letra: ")
                tupalabra += tuletra

                if tuletra not in palabra:  # comando de python que permite verificar si la letra esta o no
                    vida -= 1
                    print("Te equivocaste vuelve a intentar")
                    print("Tu tienes ", +vida, " vidas")
                if vida == 0:
                    print("Perdiste! tus intentos han acabado, la palabra era: "+palabra)
            else:
                print("Gracias por participar ")
            print(linea_punteada)
            volver_ajugar = input("¿Quieres jugar de nuevo? Si(1)/No(0):")





#main
opc = 0

ancho_linea = 72
linea_punteada = ancho_linea * '.'

print(linea_punteada)

while opc !=3:
    print "--Menu de juego--"
    print "1. Ahorcado"
    print "2. Adivina el numero"
    print "3. Terminar"

    opc = input("\nIngrese su opcion: ")

    print(linea_punteada)

    if (opc == 1):
        Ahorcado()

    elif (opc == 2):
        AdivinaElNumero()
    elif (opc == 3):
        print "Programa Terminado"
    else:
         print"Opcion Incorrecta ,La opcion no se encuentra en el menu"
    print(linea_punteada)