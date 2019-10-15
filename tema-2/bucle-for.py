# encoding: utf-8


# EJEMPLO 1
# El cuerpo del bucle se ejecuta tantas veces como elementos tenga el elemento recorrible (elementos de una lista o de range(), caracteres de una cadena, etc.). Por ejemplo:
def ejemplo1():
    print('Comienzo')
    for i in [0,1,2]:
        print 'Hola ',
    print
    print('Final')


# EJEMPLO 2
# Si la lista está vacía el bucle no se ejecuta ninguna vez
def ejemplo2():
    print('Comienzo')
    for i in []:
        print 'Hola ',
    print
    print('Final')


# Función auxiliar para poner un separador
def aux():
    print('*' * 30)


# EJEMPLO 3
# En el primer ejemplo, los valores que toma la variable no son importantes, lo que importa es que la lista tiene tres elementos y por tanto el bucle se ejecuta tres veces . El siguiente programa produciría el mismo resultado que el anterior:
def ejemplo3():
    print("Comienzo")

    for i in [1, 1, 1]:
        print "Hola ",
    print
    print("Final")


# EJEMPLO 4
# Si la variable de control no se va a utilizar en el cuerpo del bucle, como en los ejemplos anteriores, se puede utilizar el guion (_) en vez de un nombre de variable. Esta notación no tiene ninguna consecuencia con respecto al funcionamiento del programa, pero sirve de ayuda a la persona que esté leyendo el código fuente, que sabe así que los valores no se van a utilizar.
def ejemplo4():
    print('Comienzo')
    for _ in [0,1,2]:
        print 'Hola',
    print
    print('final')


# EJEMPLO 5
# En los ejemplos anteriores, la variable de control "i" no se utilizaba en el bloque de instrucciones, pero en muchos casos sí que se utiliza. Cuando se utiliza, hay que tener en cuenta que la variable de control va tomando los valores del elemento recorrible.
def ejemplo5():
    print('Comienzo')
    for i in [3,4,5]:
        print('Hola. Ahora i vale {i} y su cuadrado {i ** 2}')
    print('Final')


# EJEMPLO 6
# La lista puede contener cualquier tipo de elementos, no sólo números. El bucle se repetirá siempre tantas veces como elementos tenga la lista y la variable irá tomando los valores de uno en uno. Por ejemplo:
def ejemplo6():
    print('Comienzo')
    for i in ['Keko kaka', 'Reba', 'Archie', 1]:
        print('Hola, ahora i vale {i}')
    print('Final')


# EJEMPLO 7
# La costumbre más extendida es utilizar la letra i como nombre de la variable de control, pero se puede utilizar cualquier otro nombre válido.
def ejemplo7():
    print('Comienzo')
    for numero in [0,1,2,3]:
        print numero, '*', numero, '=', numero ** 2
    print('Final')


# EJEMPLO 8
# La variable de control puede ser una variable empleada antes del bucle. El valor que tuviera la variable no afecta a la ejecución del bucle, pero cuando termina el bucle, la variable de control conserva el último valor asignado:
def ejemplo8():
    i = 10
    print 'El bucle no ha comenzado. Ahora i vale ', i
    
    for i in [0, 1, 2, 3, 4]:
        print i, '*', i, '=', i ** 2

    print 'El bucle ha terminado. Ahora i vale', i


# EJEMPLO 9
# En vez de una lista se puede escribir una cadena, en cuyo caso la variable de control va tomando como valor cada uno de los caracteres:
def ejemplo9():
    for i in 'AMIGO':
        print 'Dame una ', i 
    print '¡AMIGO!'


# EJEMPLO 10
# En los ejemplos anteriores se ha utilizado una lista para facilitar la comprensión del funcionamiento de los bucles pero, si es posible hacerlo, se recomienda utilizar tipos range(), entre otros motivos porque durante la ejecución del programa ocupan menos memoria en el ordenador.
def ejemplo10():
    print 'Comienzo'
    for i in range(3):
        print 'Hola ',
    print
    print 'Final'


# EJEMPLO 11
# CONTADORES
# Se entiende por contador una variable que lleva la cuenta del número de veces que se ha cumplido una condición. El ejemplo siguiente es un ejemplo de programa con contador (en este caso, la variable que hace de contador es la variable cuenta):
def ejemplo11():
    print 'Comienzo'
    cuenta = 0

    for i in range (1,6):
        if i % 2 == 0:
            cuenta = cuenta +1
    print 'Desde 1 hasta 5 hay ', cuenta, ' múltiplos de 2'


# EJEMPLO 12
# ACOMULADORES
# Se entiende por acumulador una variable que acumula el resultado de una operación. El ejemplo siguiente es un ejemplo de programa con acumulador (en este caso, la variable que hace de acumulador es la variable suma):
def ejemplo12():
    suma = 0

    for i in [1,2,3,4]:
        suma = suma + i
    print 'La suma de los números del 1 al 4 es: ', suma

ejemplo1()
aux()
ejemplo2()
aux()
ejemplo3()
aux()
ejemplo4()
aux()
ejemplo5()
aux()
ejemplo6()
aux()
ejemplo7()
aux()
ejemplo8()
aux()
ejemplo9()
aux()
ejemplo10()
aux()
ejemplo11()
aux()
ejemplo12()
