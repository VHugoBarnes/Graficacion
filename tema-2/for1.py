# encoding: utf8
"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""


inicio = input('Ingrese el número inicial: ')
fin = input('Ingrese el numero final: ')


#
def _aumenta4(inicio, fin):
    
    for inicio in range(inicio, fin+1, 4):
        print inicio


_aumenta4(inicio,fin)

