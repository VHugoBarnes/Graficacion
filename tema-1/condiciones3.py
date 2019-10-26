# encoding: UTF-8

"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""

def _signo(num):
    if num > 0:
        return 'Es positivo'
    elif num < 0:
        return 'Es negativo'
    else:
        return 'Es cero'


num = input('Dame un número:')
print _signo(num)