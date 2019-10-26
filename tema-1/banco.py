# encoding: utf-8
"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""

def _cuotas(prestamo, meses):
    cuotas = prestamo / meses
    return cuotas

def _prestamo(ingresos,egresos):
    prestamo = input('Monto del prestamo: ')
    meses = input('¿Cuantos meses de pago? ')

    print 'Monto de pago por mes: ', _cuotas(prestamo,meses)


def edad():
    edad = input('Ingrese su edad: ')

    if edad >= 18:
        ingresos = input('Dame tus ingresos:')
        egresos = input('Dame tus egresos: ')

        if ingresos >= egresos:
            _prestamo(ingresos, egresos)
        else:
            print 'No es posible hacer el prestamo 😑'
    else:
        print 'No es mayor de edad'


edad()
