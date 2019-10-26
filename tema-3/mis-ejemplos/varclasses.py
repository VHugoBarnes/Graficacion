# coding: utf-8
"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""
# Programa en python para demostrar que las variables con un valor
# asignado a la declaración de una clase, son variables de clase y
# las variables dentro de los métodos y constructores son
# variables de instancia.

# Clase para estudiante de Ingeniería en Sistemas Computacionales
class ISCEstudiante:

    # Variable de clase
    materia = 'Graficación'

    # El método init o constructor
    def __init__(self, semestre):
        # Variable de instancia
        self.semestre = semestre


# Objetos de la clase de ISC
a = ISCEstudiante('Quinto Semestre')
b = ISCEstudiante('Quinto Semestre')

print a.materia  # Se imprime 'Graficación'
print b.materia  # Se imprime 'Graficación'
print a.semestre  # Se imprime 'Quinto Semestre'

# Las variables de clase también pueden
# ser accesadas usando el nombre de la clase también
print ISCEstudiante.materia