# coding=utf-8

"""
Código escrito por: Nicole Rodriguez González y Víctor Hugo Vázquez Gómez

                                                    BATALLA NAVAL

Representación de cómo se verá el juego
 COMPUTADORA                JUGADOR
  1  2  3  4               1  2  3  4
1[*][ ][ ][*]            1[ ][*][ ][ ]
2[ ][*][ ][ ]            2[ ][ ][ ][ ]
3[ ][ ][ ][ ]            3[ ][ ][*][ ]
4[ ][*][ ][ ]            4[*][*][ ][ ]

"""
import copy  # copy nos proporciona operaciones genericas de copiado
import random
import textwrap
import time

# Declaración de constantes.
DIMENSION_ = 6
TURNO_ = 4


# Imprime el mapa
def __imprimir_mapa__(jugador, mesa, dimension):
    player = 'la computadora'
    if jugador == 'u':
        player = 'el jugador'

    print "\033[1m" + 'La mesa de ' + player + ' se ve así:' + "\033[0m"
    # Imprimir el número de columna
    for i in range(dimension):
        print '   ' + str(i + 1) + '',
    print ' '

    for i in range(dimension):
        # Imprimir el número de fila
        print str(i + 1) + '',
        # Imprime los valores de las celdas
        for j in range(dimension):
            if mesa[i][j] == -1:
                print '[ ] ',  # Imprime la mesa vacía por primera vez (ésto sólo se ejecuta la primera vez)
            elif jugador == 'u':
                print mesa[i][j],  # Aquí se imprime la mesa del jugador, puede contener [] o [S]
            elif jugador == 'c':  # Si el jugador es computadora se imprime su mesa
                if mesa[i][j] == '[!] ' or mesa[i][j] == '[*] ':
                    print mesa[i][j],
                else:
                    print '[ ] ',
        print ' '


# Obtener coordenadas usuario
def __obtener_coordenada__(dimension):
    while True:
        user_input = raw_input("\033[1m" + 'Por favor, ingresa las coordenadas (columna,fila): ' + "\033[0m")
        try:
            # Verificar si el usuario ingresó 2 valores separados por coma
            coor = user_input.split(',')
            if len(coor) != 2:
                raise Exception("\033[1m" + 'Entrada invalida, pocas/muchas coordenadas' + "\033[0m")

            coor[0] = int(coor[0]) - 1
            coor[1] = int(coor[1]) - 1

            # Verifica si están dentro del limite
            if coor[0] > dimension - 1 or coor[0] < 0 or coor[1] > dimension - 1 or coor[1] < 0:
                exc = "\033[1m" + 'Entrada invalida, ingresa valores entre 1 y ', \
                      str(dimension), ' solamente.' + "\033[0m"
                raise Exception(exc)

            return coor
        except ValueError:
            print "\033[1m" + 'Entrada inválida, ingresa sólo dos coordenadas' + "\033[0m"
        except Exception as e:
            print e


# La computadora escoge por random
def __computadora_escoge__(mesa_computadora, dimension, turno):
    lista_comp = []  # Se crea una lista con la cantidad de turno que se pasen por parametro

    for i in range(dimension):
        lista_comp.append(i)  # En caso de DIMENSION_ = 8 E lista_comp = ['1','2','3','4','5','6','7','8']

    # Variable auxiliar para controlar el flujo de turnos
    m = 0

    while m < turno:
        # Se escoge un número.
        escoger_coordenada_x_comp = random.choice(lista_comp)
        escoger_coordenada_y_comp = random.choice(lista_comp)
        validacion = __validar__('c', escoger_coordenada_x_comp, escoger_coordenada_y_comp)
        if validacion:
            m = m - 1
        else:
            m = m + 1
    print "\033[1m" + 'La computadora ya colocó sus submarinos' + "\033[0m"
    return mesa_computadora


# Colocar submarino
def __colocar_submarino__(mesa, x, y):
    mesa[x][y] = '[S] '
    return mesa


# Validacion de que ya se ingresaron esas coordenadas
coordenadas_usuario = []
coordenadas_computadora = []


def __validar__(player, x, y):
    individual = str(x + 1) + str(y + 1)

    if player == 'u':
        if individual in coordenadas_usuario:
            return True
        else:
            coordenadas_usuario.append(individual)
            return False
    elif player == 'c':
        if individual in coordenadas_computadora:
            return True
        else:
            coordenadas_computadora.append(individual)
            return False


# El usuario escoge
def __usuario_escoge__(mesaus, dimension, turno):
    p = 0
    while True:

        p = p + 1

        __imprimir_mapa__('u', mesaus, dimension)

        if p > turno:
            break

        print "\033[1m" + 'Colocando un submarino: ' + "\033[0m"
        x, y = __obtener_coordenada__(dimension)  # Obtiene coordenadas (x,y) del 0 a dimension
        validacion = __validar__('u', x, y)  # Devuelve True si dicha coordenada ya fue ingresada, False si no

        # Si la coordenada ya se ingresó se resta un turno
        if validacion:
            p = p - 1
            print "\033[1m" + 'Verifica el mapa, ya hay un submarino en esa coordenada' + "\033[0m"
        else:  # Si la coordenada no se ha ingresado, se coloca el submarino en la mesa
            __colocar_submarino__(mesaus, x, y)
    raw_input("\033[1m" + 'Se han colocado todos los submarinos, presiona ENTER para continuar' + "\033[0m")

    return mesaus


# Configurar tabla de juego
def __configurar_mesa__(mesa, dmnsn):
    # Esta función rellena la mesa de dmnsn * dmnsn con -1
    for i in range(dmnsn):
        __mesa_fila__ = []
        for j in range(dmnsn):
            __mesa_fila__.append(-1)
        mesa.append(__mesa_fila__)


ataques_jugador = []
ataques_computadora = []


# Verifica si dio en el blanco
def __validar_ataque__(mesa, player, x, y):
    """
    __validar_ataque__ es una función que entra después de que las coordenadas hayan sido ingresadas para el ataque.
    Retorna un número (-1,0,1) dependiendo a dónde fue el misil
    :param mesa: De qué mesa se trata
    :param player: A qué jugador atacar. c = computadora; u = usuario
    :param x: La coordenada x
    :param y: La coordenada y
    :return: -1 si la coordenada ya se ingresó anteriormente
    :return: 1 si la coordenada ingresada dió en el blanco
    :return: 0 si la coordenada ingresada no dió en el blanco
    """
    coordenada = str(x + 1) + str(y + 1)
    if player == 'c':  # Turno del usuario
        if coordenada in ataques_jugador:
            return -1
        else:
            if coordenada in coordenadas_computadora:
                mesa[x][y] = '[!] '
                ataques_jugador.append(coordenada)
                return 1
            else:
                mesa[x][y] = '[*] '
                ataques_jugador.append(coordenada)
                return 0
    elif player == 'u':  # Turno de la computadora
        if coordenada in ataques_computadora:
            return -1
        else:
            if coordenada in coordenadas_usuario:
                mesa[x][y] = '[!] '
                ataques_computadora.append(coordenada)
                return 1
            else:
                mesa[x][y] = '[*] '
                ataques_computadora.append(coordenada)
                return 0


# El jugador ingresa coordendas para mandar misil
def __jugador_ataca__(mesacomp, dimension):
    """
    Obtiene las coordenadas del usuario y hace el ataque.
    Si el jugador da en el blanco, cambia a  [!] y suma punto.
    :param mesacomp:
    :param dimension:
    :return:
    """
    global pts_jugador
    while True:
        x, y = __obtener_coordenada__(dimension)

        validacion = __validar_ataque__(mesacomp, 'c', x, y)

        if validacion == -1:
            print "\033[1m" + 'Ya se ha mandado un mísil a dicha coordenada, intenta de nuevo' + "\033[0m"
        elif validacion == 0:
            print "\033[1m" + 'Mísil mandado a ' + str(x + 1) + ',' + str(y + 1) + "\033[0m"
            time.sleep(1)
            print "\033[1m" + 'El mísil no dió en el blanco :(' + "\033[0m"
            return mesacomp
        elif validacion == 1:
            print "\033[1m" + 'Mísil mandado a ' + str(x + 1) + ',' + str(y + 1) + "\033[0m"
            time.sleep(1)
            print "\033[1m" + '¡El mísil dió en el blanco!' + "\033[0m"
            pts_jugador = pts_jugador + 1
            return mesacomp


# La computadora elige aleatoriamente las coordenadas
def __computadora_ataca__(mesaus, dimension):
    global pts_computadora

    intento = True

    while intento:
        # Se elige aleatoriamente las coordenadas
        x = random.randint(0, dimension - 1)
        y = random.randint(0, dimension - 1)

        validacion = __validar_ataque__(mesaus, 'u', x, y)

        if validacion == -1:
            print "\033[1m" + 'La computadora ya mandó un mísil a esa coordenada, lo volverá a intentar' + "\033[0m"
            intento = True
        elif validacion == 0:
            print "\033[1m" + 'Mísil mandado a ' + str(x + 1) + ',' + str(y + 1) + "\033[0m"
            time.sleep(1)
            print "\033[1m" + 'Excelente, la computadora no dió en el blanco' + "\033[0m"
            intento = False
            return mesaus
        elif validacion == 1:
            print "\033[1m" + 'Mísil mandado a ' + str(x + 1) + ',' + str(y + 1) + "\033[0m"
            time.sleep(1)
            print "\033[1m" + 'La computadora ha destruido uno de tus submarinos' + "\033[0m"
            pts_computadora = pts_computadora + 1
            intento = False
            return mesaus


def __juego__():
    print "\033[1m" + '== BATALLA NAVAL ==' + "\033[0m"

    msg = ('Instrucciones: '
           'Hay dos mesas de la misma dimensión y te enfrentaras a un enemigo desconocido :3 '
           'Primero ingresaras las coordenadas donde se localizara tus submarinos (columna,fila) Ej. 3,2 '
           'posteriormente, el enemigo colocara sus submarinos, por defecto estaran ocultos para ti.'
           ' El objetivo es mandar mísiles con las coordenadas que ingresaste para atacar al enemigo.'
           ' Gana el primero en derribar todos los submarinos')
    mesa = []
    __configurar_mesa__(mesa, DIMENSION_)  # Configura una mesa de DIMENSION_ * DIMENSION_
    print(textwrap.fill(msg, width=112))
    # Configurar la mesa del usuario y computadora. Se copia la mesa a mesa_usuario y mesa_computadora
    mesa_usuario = copy.deepcopy(mesa)
    mesa_computadora = copy.deepcopy(mesa)

    #                                           COLOCACIÓN DE SUBMARINOS
    # El usuario escoge coordenadas
    mesa_usuario = __usuario_escoge__(mesa_usuario, DIMENSION_, TURNO_)
    # print coordenadas_usuario
    # La computadora escoge coordenadas
    mesa_computadora = __computadora_escoge__(mesa_computadora, DIMENSION_, TURNO_)
    # print coordenadas_computadora

    # Main loop
    while 1:

        #
        #                                               Turno del jugador
        # Jugador ingresa coordenadas para atacar a la computadora
        mesa_computadora = __jugador_ataca__(mesa_computadora,
                                             DIMENSION_)  # Por eso se está modificando la mesa_computadora
        # Si pasó la validación, pasa a atacar

        if pts_jugador == TURNO_:
            print "\033[1m" + 'Has derrivado todos los submarinos de la computadora, ¡HAS GANADO!' + "\033[0m"
            raw_input("\033[1m" + 'Presiona ENTER para terminar' + "\033[0m")
            quit()

        # Muestra el mapa enemigo, si dió en el blanco [!], si no, [*]
        __imprimir_mapa__('c', mesa_computadora, DIMENSION_)
        raw_input('Presiona ENTER para continuar')
        # Si dió en el blanco[!], se incrementa un punto
        #
        #                                               Turno del enemigo
        # Computadora 'adivina' las coordenadas
        mesa_usuario = __computadora_ataca__(mesa_usuario, DIMENSION_)
        # Se valida si la PC ya atacó a esa coordenada
        #
        if pts_computadora == TURNO_:
            print "\033[1m" + 'La computadora ha derrivado todos tus submarinos, has perdido.' + "\033[0m"
            raw_input("\033[1m" + 'Presiona ENTER para terminar' + "\033[0m")
            quit()
        # Si pasó la validación, pasa a atacar
        # Muestra el mapa enemigo, si dio en blanco [!], si no, [o]
        __imprimir_mapa__('u', mesa_usuario, DIMENSION_)
        # Si dió en el blanco[!], se incrementa un punto
        #


if __name__ == '__main__':
    pts_jugador = 0
    pts_computadora = 0
    __juego__()
