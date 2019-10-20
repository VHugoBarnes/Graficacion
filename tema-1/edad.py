# encoding: utf-8

print('¿Cuantos años tienes?')
edad = input()

if edad >= 0 and edad < 18:
    print('Eres un niño')
elif edad < 0:
    print('No existes 🐸👌🏿')
elif edad >= 18 and edad < 27:
    print('Eres un joven')
elif edad >= 27 and edad < 60:
    print('Eres un adulto')
else: 
    print('Eres de la tercera edad')
