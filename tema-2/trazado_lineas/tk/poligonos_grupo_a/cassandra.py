# -*- coding: utf-8 -*-
"""
    Programa escrito por: Cassandra González
"""
from Tkinter import *
import tkColorChooser #libreria para obtener gama de colores

class Cassandra:
    def mostrar(self, titulo):
        # a = tkColorChooser.askcolor()
        v1 = Toplevel()  # ventana hija
        v1.title(titulo)
        v1.protocol('wn_DELETE_WINDOW', "onexit")  # para cerrar con la tachita la ventana
        v1.geometry('300x250')

        panel = Canvas(v1, width=220, height=460, bg='white')  # dibujar algo, un lienzo, figuras
        panel.pack(expand=YES, fill=BOTH)  # para expandir la ventana
        # Cuerpo completo
        panel.create_polygon(20, 10, 20, 10, 50, 10, 50, 20, 100, 20, 100, 10, 130, 10, 130, 20, 140, 20, 140, 50, 130,
                             50, 130, 60, 120, 60, 120, 150, 110, 50, 110, 70, 120, 70, 120, 110, 130, 110, 130, 120,
                             140, 120, 140, 130, 150,
                             130, 150, 140, 160, 140, 160, 150, 180, 150, 180, 130, 170, 130, 170, 120, 160, 120, 160,
                             100, 180, 100,
                             180, 110, 190, 120, 190, 120, 200, 120, 220, 130, 210, 130, 210, 210, 70, 210, 70, 190, 80,
                             190, 80, 160, 70,
                             160, 70, 150, 60, 150, 60, 130, 50, 130, 50, 120, 40, 120, 40, 110, 30, 110, 30, 70, 40,
                             70, 40, 50, 30, 50, 30,
                             60, 20, 60, 20, 50, 10, 50, 10, 20, 20, 20, 20, 10, width=7, fill="black", outline="black")
        # Color cafe oreja izq
        panel.create_polygon(50, 20, 50, 30, 40, 30, 40, 40, 30, 40, 30, 50, 20, 50, 20, 20, 50, 20, width=5,
                             fill="brown", outline="brown")

        # Color cafe oreja derecha
        panel.create_polygon(130, 20, 130, 50, 120, 50, 120, 40, 110, 40, 110, 30, 100, 30, 100, 20, 130, 20, width=5,
                             fill="brown", outline="brown")

        # Cara
        panel.create_polygon(100, 30, 50, 30, 50, 70, 40, 70, 40, 110, 50, 110, 50, 120, 70, 120, 70, 110, 80, 110, 80,
                             120,
                             100, 120, 100, 110, 110, 110, 110, 70, 100, 70, 100, 30, width=5, fill="white",
                             outline="white")

        # Ojo izq1
        panel.create_polygon(60, 50, 60, 60, 70, 60, 70, 50, 60, 50, width=5, fill="black", outline="black")

        # Mancha en el ojo
        panel.create_polygon(100, 40, 70, 40, 70, 70, 100, 70, 100, 40, width=6, fill="brown", outline="brown")

        # Ojo derecho
        panel.create_polygon(80, 50, 80, 60, 90, 60, 90, 50, 80, 50, width=5, fill="black", outline="black")

        # Nariz
        panel.create_polygon(90, 80, 90, 100, 60, 100, 60, 80, 90, 80, width=6, fill="black", outline="black")

        # Lengua
        panel.create_polygon(80, 120, 70, 120, 70, 150, 80, 150, 80, 120, width=5, fill="pink", outline="pink")

        # Cuerpo mitad 1
        panel.create_polygon(120, 110, 120, 190, 130, 190, 130, 200, 110, 200, 110, 150, 100, 150, 100, 200, 80, 200,
                             80, 190,
                             90, 190, 90, 130, 100, 130, 100, 120, 110, 120, 110, 110, 120, 110, width=5, fill="white",
                             outline="white")

        # Cuerpo mitad 2
        panel.create_polygon(200, 130, 200, 200, 170, 200, 170, 190, 180, 190, 180, 180, 170, 180, 170, 170, 160, 190,
                             160, 200, 140, 200,
                             140, 190, 130, 190, 130, 160, 180, 160, 180, 150, 190, 150, 190, 130, 200, 130, width=5,
                             fill="white", outline="white")

        # Cola
        panel.create_polygon(180, 110, 170, 110, 170, 120, 180, 120, 180, 130, 190, 130, 190, 120, 180, 120, 180, 110,
                             width=5, fill="brown", outline="brown")

        # Mancha lomo
        panel.create_polygon(130, 120, 120, 120, 120, 150, 130, 150, 130, 160, 160, 160, 160, 150, 150, 150,
                             150, 140, 140, 140, 140, 130, 140, 130, 140, 120, 120, 120, width=3, fill="brown",
                             outline="brown")