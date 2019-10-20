# encoding: UTF-8


def _signo(num):
    if num > 0:
        return 'Es positivo'
    elif num < 0:
        return 'Es negativo'
    else:
        return 'Es cero'


num = input('Dame un número:')
print _signo(num)