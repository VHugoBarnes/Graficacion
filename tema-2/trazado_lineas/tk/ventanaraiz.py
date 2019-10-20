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

        boton1 = Button(ventana, text='Checkbutton', bg=color_boton, fg=color_letra, command=lambda: self.ventanaHija(1))
        boton2 = Button(ventana, text='Entry', bg=color_boton, fg=color_letra, command=lambda: self.ventanaHija(2))
        boton3 = Button(ventana, text='Label', bg=color_boton, fg=color_letra, command=lambda: self.ventanaHija(3))
        boton4 = Button(ventana, text='Listbox', bg=color_boton, fg=color_letra, command=lambda: self.ventanaHija(4))
        boton5 = Button(ventana, text='Spinbox', bg=color_boton, fg=color_letra, command=lambda: self.ventanaHija(5))
        boton6 = Button(ventana, text='Personalizado', bg=color_boton, fg=color_letra, command=lambda: self.ventanaHija(6))

        boton1.grid(column=1, row=1, ipadx=49, pady=3, padx=3)
        boton2.grid(column=1, row=2, ipadx=49, pady=3, padx=3)
        boton3.grid(column=1, row=3, ipadx=49, pady=3, padx=3)
        boton4.grid(column=1, row=4, ipadx=49, pady=3, padx=3)
        boton5.grid(column=1, row=5, ipadx=49, pady=3, padx=3)
        boton6.grid(column=1, row=6, ipadx=49, pady=3, padx=3)