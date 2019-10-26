# encoding: UTF-8

"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""

def _iniciar(monto):
    dulce = raw_input('Elija la letra: ')

    if dulce == 'a':
        precioProducto = 2.5
        print 'Su cambio es: ', _calcularCambio(precioProducto, monto)
    elif dulce == 'b':
        precioProducto = 1.4 
        print 'Su cambio es: ', _calcularCambio(precioProducto, monto)
    elif dulce == 'c':
        precioProducto = 1.2 
        print 'Su cambio es: ', _calcularCambio(precioProducto, monto)


def _calcularCambio(precioProducto, monto):
    return monto - precioProducto


monto = input('Ingrese el monto: ')

if monto < 5:
    _iniciar(monto)
else:
    print 'Monto debe ser menor a $5'