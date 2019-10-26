#!/usr/bin/python
# -*- coding: utf-8 -*-
# www.pythondiario.com

from Tkinter import *
from tkMessageBox import *


def pregunta():
    showerror("Pregunta", "Discuple, no hay preguntas disponibles")


def devolucion():
    if askyesno('Verificar', '¿Realmente quiere salir?'):
        showwarning('Si', 'No está implementado')
    else:
        showinfo('No', 'Salir fue cancelado')


Button(text='Salir', command=devolucion).pack(fill=X)
Button(text='Pregunta', command=pregunta).pack(fill=X)
mainloop()