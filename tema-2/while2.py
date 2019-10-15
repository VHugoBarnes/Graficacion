# encoding: utf8


def _sacarimpar(numeroin, numerofin):
    while numeroin <= numerofin:
        residuo = numeroin % 2

        if residuo != 0:
            print 'El número es impar', numeroin
        else:
            print 'El número es par', numeroin
        
        numeroin += numeroin


def menu():
    numeroin = input('Dame el número inicial: ')
    numerofin = input('Hasta que número saber impar: ')
    _sacarimpar(numeroin,numerofin)


menu()
