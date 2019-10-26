# -*- coding: utf-8 -*-
# Programa escrito por: yolyrdz.blogspot.com
import sys
from Tkinter import *
import tkMessageBox

def valida():
    if len(ent_usuario.get()) < 6 :
        tkMessageBox.showerror("INCORRECTO TAMAÑO","TIENE QUE SE MAYOR A 6 CARACTERES")

    if len(ent_usuario.get()) > 12:
        tkMessageBox.showerror("INCORRECTO TAMAÑO", "TIENE QUE MENOR A 12 CARACTERES")





ventana= Tk()
ventana.title ('Validadando ContraseNas')
ventana.geometry('500x300')

vp = Frame(ventana) #estamos utilizando el objeto frame
vp.grid(column=0, row=0, padx =(50,50), pady=(10,10))
vp.columnconfigure(0, weigh=1)
vp.rowconfigure(0, weight =1)

etiqueta= Label(vp, text='Dame el nombre del Ususarios: ')
etiqueta.grid(row=2, column=4, padx=(20,20), pady=(20,20))

usuario=""
ent_usuario = Entry(vp, width=12,  textvariable= usuario)
ent_usuario.grid(row=2, column=5, padx=(20,20), pady=(20,20))

etiqueta1= Label(vp, text='Dame la contraseña: ')
etiqueta1.grid(row=4, column=4, padx=(20,20), pady=(20,20))

contrasena=""
ent_contrasena = Entry(vp, width=12, show='*', textvariable= contrasena)
ent_contrasena.grid(row=4, column=5, padx=(20,20), pady=(20,20))


boton=Button(vp, text='Validar', command=valida )
boton.grid(row=6,column=3,padx=(20,20), pady=(20,20))