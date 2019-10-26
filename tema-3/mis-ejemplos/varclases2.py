# coding: utf-8
"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""
# Programa para mostrar que podemos crear
# variables de instancia dentro de metodos.

# Clase para estudiante de Ingeniería en Sistemas Computacionales.
class ISCEstudiante:

    #Variable de clase
    materia = 'Graficación'

    # El método init o constructor
    def __init__(self, semestre):
        # Variable de instancia
        self.semestre = semestre

    # Añade una variable de instancia
    def set_edad(self, edad):
        self.edad = edad

    # Devuelve la variable de instancia
    def get_edad(self):
        return self.edad


# Código de manejo
a = ISCEstudiante('Quinto Semestre')
a.set_edad(20)
print a.get_edad()