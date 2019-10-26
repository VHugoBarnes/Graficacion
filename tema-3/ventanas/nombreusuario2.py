# -*- coding: utf-8 -*-
# Programa escrito por: yolyrdz.blogspot.com
import sys
from Tkinter import *
import tkMessageBox

def valida2():
    bandera = 0  # se pondra en 1 si encuentra espacios
    bandera1 = 0 # se pondra en uno si encuentra mayusculas
    bandera2 = 0 # se pondra en uno si encuentra minusculas
    bandera3 = 0 # se pondra en uno si encuentra un numero
    bandera4 = 0 # cambia a uno si tiene un espacio y es menor a 8 caract

    palabra= ent_pass.get()
    y = palabra.isalnum()  # si es alfanumérica retona True
    print y
    for i in palabra:  # ciclo for que recorre caracter por caracter en la contraseña
        if i.isspace() == True:
            print 'tiene espacio'
            print 'caraacter:',i
            bandera = 1
            print bandera
        if i.isupper() == True:
            print 'tiene mayuscualas'
            print 'caracter: ',i
            bandera1 = 1
            print bandera1
        if i.islower() == True:
            print ' tiene minusculas'
            print 'caracter:',i
            bandera2 = 1
            print bandera2
        if i.isdigit() == True:
            print 'tiene numero'
            print 'caracter: ',i
            bandera3 = 1
            print bandera3
    if bandera == 1:
        print "el password no puede tener espacios"
    if len(ent_pass.get()) < 8 and bandera==1:
        print("el password no puede ser menor de 8 caracteres")
        bandera4 = 1
#La contraseña elegida no es segura: debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico
    if bandera == 0 and bandera1 == 1 and bandera2 == 1 and bandera3 == 1 and y == False and bandera4 == 0:
        print("la contraseña es segura:  tiene lestras mayusculas, minusculas, numeros y al menos un caracter no alfanumerico")
    else:
        print (" la contraseña no es segura")


def validar():
       if len(ent_usuario.get()) < 6 :
         tkMessageBox.showerror('Error', 'El usuario debe tener al menos 6 caracteres')
       if (ent_usuario.get()).isalnum() == FALSE :
         tkMessageBox.showerror('Error', 'El usuario debe tener solo numeros o letras')
       if len(ent_usuario.get()) > 12 :
         tkMessageBox.showerror('Error', 'El usuario no puede tener mas de 12 caracteres')
       if len(ent_usuario.get()) > 5 and len(ent_usuario.get()) < 12 and (ent_usuario.get()).isalnum() == TRUE:
           tkMessageBox.showinfo('usuarios aceptado', 'El usuario es correcto')




ventana= Tk()
ventana.title('Validar Password')
ventana. geometry('600x400')

vp = Frame(ventana) #estamos utilizando el objeto frame
vp.grid(column=0, row=0, padx =(50,50), pady=(10,10))
vp.columnconfigure(0, weigh=1)
vp.rowconfigure(0, weight =1)

etiqueta = Label(vp,text='Ingrese el nombre de Usuario: ')
etiqueta.grid(row=2, column=4, padx=(20,20), pady=(20,20))

usuario = ""
ent_usuario = Entry(vp, width=12, textvariable=usuario)
ent_usuario.grid(row=2, column=5, padx=(20,20), pady=(20,20))

Boton = Button(vp, text='Validar usuario', command= validar)
Boton.grid(row=2, column=6, padx=(20,20), pady=(20,20))

#etiqueta3= Label(vp, text="El password elegido debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico ")
#etiqueta3.grid(row=3, column=6, padx=(20,20), pady=(20,20))

etiqueta2 = Label(vp, text='Ingrese el Password: ')
etiqueta2.grid(row=4, column=4, padx=(20, 20), pady=(20, 20))

password = ""
ent_pass = Entry(vp, width=10,  textvariable=password)
ent_pass.grid(row=4, column=5)

Boton2 = Button(vp, text='Validar passw:', command=valida2)
Boton2.grid(row=4, column=6, padx=(20,20), pady=(20,20))

ventana.mainloop()