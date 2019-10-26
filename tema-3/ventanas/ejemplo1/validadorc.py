# -*- coding: utf-8 -*-
# Programa escrito por Alfredo Santos y Cynthia Barron
from Tkinter import *
import tkMessageBox
import userc as uv
import passwordc as pv

user_validator = uv.usuario_validar()
pass_validator = pv.password_validar()

def validation():
    cuser = user.get()
    cpasword = pasword.get()
    correcto = False


    if correcto == False:
        if not user_validator.validar_usuario(cuser):
            for error in user_validator.errors:
                tkMessageBox.showinfo("Aviso error usuario",error)
                correcto = False

                user_validator.errors.remove(error)
        else:
            correcto = True
            if correcto == True:
                if not pass_validator.validar_password(cpasword):
                    for error in pass_validator.errors:
                        tkMessageBox.showinfo("Aviso error contraseña",error)
                        correcto = True
                        pass_validator.errors.remove(error)
                else:
                    correcto = False
                    tkMessageBox.showinfo("Aviso", "Usuario y contraseña creados exitosamente")

raiz=Tk()
raiz.title("ventana primaria")
raiz.resizable(1,1) #para permitir agrandar o no el ancho o la altura con el moyuse
# raiz.iconbitmap("descarga.ico")
#raiz.geometry("500x600")
raiz.config(bg="cyan")
raiz.config(bd=15)
raiz.config(relief="groove")

miFrame=Frame(raiz)
miFrame.pack()
miFrame.config(bg="pink")
miFrame.config(bd=10)
miFrame.config(relief="sunken")
miFrame.config(cursor="hand2")

miLabel1=Label(miFrame, text="Ingrese sus datos", fg="red",bg="pink",font=("Arial",18)).grid(row=0,column=0,pady="4")
nombreusuarioLabel=Label(miFrame, text="Nombre usuario: ",bg="pink").grid(row=3,column=0, sticky="w",pady="1")
contrasenaLabel=Label(miFrame, text="Contraseña: ",bg="pink").grid(row=4,column=0,sticky="w",pady="1")

user=StringVar()
pasword=StringVar()


cuadronombreusuario=Entry(miFrame, textvariable=user)
cuadronombreusuario.grid(row=3,column=1,pady="1")
cuadronombreusuario.config(fg="blue", justify="center")

cuadrocontrasena=Entry(miFrame, textvariable=pasword)
cuadrocontrasena.grid(row=4,column=1,pady="1")
cuadrocontrasena.config(show="*",fg="blue", justify="center")

botonEnvio=Button(raiz, text= "Enviar",command=validation)
botonEnvio.pack()


raiz.mainloop()