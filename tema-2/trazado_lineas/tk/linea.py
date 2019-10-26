# coding: utf-8
"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""
from Tkinter import*
import tkColorChooser #libreria para obtener la gama de colores

v0=Tk()
v0.iconbitmap('char.ico')
v0.title('Ventana principal')
v0.config(bg='purple')
v0.geometry("500x500")


def mostrar(num):
    a = tkColorChooser.askcolor()
    v1 = Toplevel(v0)
    v1.title('Ventana hija')
    v1.protocol('wn_DELETE_WINDOW','onexit')
    v1.geometry('300x300')
    if num == 1:
        canvas1 = Canvas(v1,width=200,height=200,bg='white')
        canvas1.pack(expand=YES,fill=BOTH)
        canvas1.create_line(0,200,200,0, width=10, fill=str(a[1]))
    elif num == 2:
        canvas2 = Canvas(v1,width=200,height=200,bg='white')
        canvas2.pack(expand=YES,fill=BOTH)
        canvas2.create_rectangle(10,200,200,10, width=10, fill=str(a[1]))
    elif num == 3:
        canvas2 = Canvas(v1, width=200, height=200, bg='white')
        canvas2.pack(expand=YES, fill=BOTH)
        canvas2.create_oval(0, 300, 300, 0, width=10, fill=str(a[1]))
    elif num == 4:
        canvas4 = Canvas(v1, width=200, height=200, bg='white')
        canvas4.pack(expand=YES, fill=BOTH)
        puntos = [400, 210, 580, 480, 210, 300, 580, 300, 210, 480]  # Estrella
        canvas4.create_polygon(puntos,fill=str(a[1]), dash=(5, 3))



def ocultar(ventana):ventana.destroy()
def ejecutar(f):v0.after(200,f)

b0=Button(v0, text='Abrir ventana con linea', command=lambda:ejecutar(mostrar(1)))
b0.grid(row=1, column=1)


b1=Button(v0, text='Abrir ventana con cuadro', command=lambda:ejecutar(mostrar(2)))
b1.grid(row=1, column=2)

b2=Button(v0, text='Abrir ventana con circulo', command=lambda:ejecutar(mostrar(3)))
b2.grid(row=1, column=3)

b3=Button(v0, text='Abrir ventana con poligono', command=lambda:ejecutar(mostrar(4)))
b3.grid(row=2, column=1)

v0.mainloop()