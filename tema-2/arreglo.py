# coding=utf-8
"""
                                                    GRAFICACIÓN
                                                    24/09/2019
PROGRAMA QUE MANEJA DISTINTOS TIPOS DE LISTAS

1.- Listas con números
2.- Listas con palabras
3.- Listas con los días de la semana

Menú Arreglo

1) Ingresar números y guardar en arreglo <
2) Desplegar arreglo de números normal <
3) Ordenar arreglo a la inversa y desplegar
4) Ordenar arreglo ascendente
5) Borrar arreglo
6) Salir

Se toman 5 datos por definición

"""

# define la lista principal y las posiciones de la lista
lista = []
TIMES_ = 5

# 1.1 Ingresar datos 'str'
def __char_input__():
    if len(lista) < TIMES_:
        for i in range(TIMES_):
            print 'Ingresa el dato ', i + 1, ': ',
            dato = raw_input().lower()  # permuto los datos a minusculas para mejor manejo :)
            lista.append(dato)
    else:
        raise IndexError('¡La lista ya contiene los 5 elementos!')  # Excepción lanzada cuando el índice de
                                                                    # la sequencia está fuera de rango

# 1.2 Ingresar datos 'int'
def __int_input__():
    if len(lista) < TIMES_:
        for i in range(TIMES_):
            print 'Ingresa el número ', i + 1, ': ',
            numero = int(input())
            lista.append(numero)
    else:
        raise IndexError('¡La lista ya contiene los 5 elementos!')  # Excepción lanzada cuando el índice de
                                                                    # la sequencia está fuera de rango

# 1. Ingresa datos a la lista
def __list_input__(opt=1):
    print 'Ingresa', TIMES_, ' números:'
    if opt == 1:    # Si la opción es con números.
        __int_input__()
    elif opt == 2 or opt == 3:  # Si la opción es con palabras o con días de la semana.
        __char_input__()


# 2. Imprime los datos de la lista
def __list_output__(l):
    print str(l)[1:-1]  # Los imprime de la siguiente manera: 'Keko Kaka', 4, 'KKB', 'No tengo nada que hacer'


# 3/4.1 Ordena los días de la semana
def __day_sort__(l=[], orden=False):
    """
    Aquí creo que está la chicha del programa jeje.

    Cree un diccionario donde escribí los días de la semana y les dí un valor del 1 al 7 según su orden.
    retorna un método sorted con la lista, como llave para ordenar la constante DIAS_ORDENADOS_ y un parámetro
    opcional reverse.

    :param l: Toma una lista como parametro
    :param orden: El orden de ordenamiento, False = Ascendente; True = Descendente
    :return: Imprime en pantalla la lista ordenada con el método sorted()
    """
    DIAS_ORDENADOS_ = {'domingo':1, 'lunes':2, 'martes':3, 'miercoles':4, 'jueves':5, 'viernes':6, 'sabado':7}
    return sorted(l,key=DIAS_ORDENADOS_.get,reverse=orden)

# 3. Ordena los datos de forma descendente y los imprime
def __reverse_sort__(opt=1):
    if opt == 1 or opt == 2:
        lista.sort(reverse=True)
        __list_output__(lista)
    elif opt == 3:
        print __day_sort__(lista,orden=True)


# 4. Ordena los datos
def __sort__(opt=1):
    if opt == 1 or opt == 2:   # Ordenar números y texto se hace fácil con .sort() :p
        lista.sort()
        __list_output__(lista)
    elif opt == 3:  # Espero que funcione
        print __day_sort__(lista)


# 5. Elimina los elementos de la lista
def __delete_list__():
    del lista[:]

# 0. Menú 🐸👌🏿
def _menu(tipo = 1):
    intervalo = True

    while intervalo:
        print 'Menú Arreglo'
        print '1.- Ingresar datos y guardar en arreglo.'
        print '2.- Desplegar arreglo de datos normal.'
        print '3.- Ordenar arreglo a la inversa y desplegar.'
        print '4.- Ordenar arreglo ascendente.'
        print '5.- Borrar arreglo.'
        print '6.- Salir'

        opcion = int(input(''))

        if opcion == 1:
            __list_input__(opt=tipo)
        elif opcion == 2:
            __list_output__(lista)
        elif opcion == 3:
            __reverse_sort__(opt=tipo)
        elif opcion == 4:
            __sort__(opt=tipo)
        elif opcion == 5:
            __delete_list__()
        elif opcion == 6:
            exit()
        else:
            print 'Opción incorrecta'
            intervalo = False

        print ''
        print '¿Realizar otra operación? [Y/N]'
        respuesta = raw_input().upper()
        if respuesta != 'Y':
            intervalo = False


# -1. Main
if __name__ == '__main__':

    print '=== LISTAS ==='
    print '1.- Listas con números.'
    print '2.- Listas con palabras.'
    print '3.- Listas con los días de la semana.'
    option = int(input(''))

    if option in [1,2,3]:
        _menu(tipo=option)
    else:
        print 'Opción invalida, ¡sólo tienes tres opciones!'