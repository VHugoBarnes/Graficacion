# encoding: utf8

# variable global
global array
array = []


# ingresar a la lista
def _ingresararray():
    print 'Ingrese cinco nombres: '
    i = 0

    while i < 5:
        print 'Ingrese el ', i, 'nombre: ',
        nombre = raw_input()
        i += 1


# main
if __name__ == '__main__':
    opcion = 0

    while opcion != 2:
        print 'Programa con arreglo'
        print 'Menú'
        print '1.- Método para ingresar datos y desplegar'
        print '2.- Salir'

        opcion = input('\nIngrese la opción: ')

        if opcion == 1:
            _ingresararray()
        elif opcion == 2:
            # salir
            exit()
        else:
            print 'Opción incorrecta'

