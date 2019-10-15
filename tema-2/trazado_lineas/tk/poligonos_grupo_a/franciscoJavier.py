# coding=utf-8
#Codigo de un Ganso
#By: Francisco Javier Muñoz Rios

from Tkinter import *

class FranciscoJavier:
    def funcion(self, figura):
        vs = Toplevel()
        vs.configure(bg="gray")
        vs.title(figura)
        # Ganso
        panel = Canvas(vs, width=600, height=500, bg="light blue")
        panel.pack()
        # Pie1
        panel.create_polygon((70, 180),
                             (60, 170),
                             (90, 170),
                             width=1, fill="#FFFF00", outline="black")

        # pie2
        panel.create_polygon((100, 180),
                             (90, 170),
                             (120, 170),
                             fill="yellow", outline="black", width=1)
        # pierna1
        panel.create_line((90, 170),
                          (90, 160),
                          fill="black", width=1)
        # pierna2
        panel.create_line((120, 170),
                          (110, 160),
                          fill="black", width=1)
        # cuerpo
        panel.create_polygon((50, 50), (60, 40), (80, 40),
                             (90, 60), (90, 80), (70, 100),
                             (90, 100), (120, 120), (140, 120),
                             (110, 160), (90, 160), (50, 130),
                             (50, 100), (70, 80), (70, 60),
                             fill="gray", outline="black", width=1)
        # pico
        panel.create_polygon((40, 60),
                             (70, 60),
                             (50, 50),
                             width=1, outline="black", fill="yellow")
        # ojo
        panel.create_polygon((60, 40), (60, 50), (70, 50), width=1, outline="black", fill="yellow")