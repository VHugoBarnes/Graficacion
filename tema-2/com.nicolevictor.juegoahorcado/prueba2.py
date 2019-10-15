# coding=utf-8
palabra = 'holanda'
cantidadletras = len(palabra)

respuesta = raw_input("Ingresa una letra: ")
tmp = []

for i in palabra:
    tmp.append('_ ')

brackets = '{}' * cantidadletras
print brackets.format(*tmp)

# var = '{}{}{}{}{}{}{}'.format('_, _, _, _, _, _, _')
# print var
# _ _ _ _ _ _ _

if respuesta in palabra:
    print 'Correcto'
    for i in range(0, cantidadletras):
        if palabra[i] == respuesta:
            tmp[i] = respuesta
    print brackets.format(*tmp)