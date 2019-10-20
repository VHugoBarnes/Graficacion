# encoding: utf-8


def _mayor(num1,num2):
    if num2 % num1 == 0:
        print num1, ' es multiplo de ', num2
    else:
        print num1, ' no es multiplo de ', num2


num1 = input('Dame el primer número:')
num2 = input('Dame el segundo número:')
_mayor(num1,num2)
