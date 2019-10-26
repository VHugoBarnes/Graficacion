"""
    Programa escrito por: Luis Molina
"""
from Tkinter import *

class Luis:
    def funcion(self, nombre):
        vs = Toplevel()
        vs.configure(bg="gray")
        vs.title(nombre)
        panel = Canvas(vs, width=1200, height=650, bg="gray")
        panel.pack()
        # cuerpo
        panel.create_polygon(40, 30, 60, 30, 60, 40, 40, 60, 30, 60, 30, 90, 50, 70, 70, 70, 90, 90, 90, 50, 110, 70,
                             150, 70, 170, 50, 170, 110, 160, 120, 140, 130, 120, 130, 100, 120, 90, 110, 90, 140, 100,
                             140, 100, 160, 70, 160, 70, 120, 50, 120, 40, 130, 40, 140, 60, 140, 60, 160, 20, 160, 0,
                             100, 10, 60,
                             width=10, fill="#e0af77", outline="black")
        # ojos
        panel.create_polygon(100, 100, 100, 80, 120, 80, 120, 100, width=1, fill="white", outline="black")
        panel.create_polygon(140, 80, 140, 100, 160, 100, 160, 80, width=1, fill="white", outline="black")