# coding: utf-8

from Tkinter import *

class VentanaRaiz:

    def __init__(self):
        pass

    def ventanaHija(self, num):
        if num == 1:
            pass

    def ventanaRaiz(self):
        ventana = Tk()
        ventana.geometry('500x225')
        ventana.configure(bg='#d3abf5')
        ventana.title('Componentes Tkinter')

        color_boton = "#9C7FB5"
        color_letra = "#2E2536"

        titulo = Text(font='Arial', foreground='black')
        titulo.insert(INSERT, 'Pizzas Don Kekino')

        titulo.grid(column=2, row=1)

        ventana.mainloop()
