from Tkinter import*
import tkColorChooser

v0=Tk()
v0.title('Ventana principal')
v0.config(bg='snow')
v0.geometry("200x200")
#v0.iconbitmap("c.png")

def mostrar(num):
    v1=Toplevel(v0)
    v1.title('ventana hija')
    v1.protocol('wn_DELETE_WINDOW', "onexit")
    v1.geometry("300x400")

    if num == 1:
        f1=Canvas(v1, width=200,height=200,bg='white')
        f1.pack(expand=YES, fill=BOTH)
        #cuerpo
        f1.create_polygon(110, 50, 190, 50, 190, 130, 230, 130, 230, 250, 190, 250, 190, 330, 110, 330, 110, 250, 70, 250, 70, 130, 110, 130, 110, 50,   width=10, fill='tan1')
        #cara
        f1.create_polygon(110, 50, 190, 50, 190, 80, 180, 80, 180, 70, 120, 70, 120, 80, 110, 80, 110, 50,  width=1, fill='saddle brown')
        f1.create_polygon(120,90, 130, 90, 130, 100, 120, 100, 120,90, width=1, fill='snow')
        f1.create_polygon(130, 90, 140, 90, 140, 100, 130, 100, 130, 90, width=1, fill='magenta4')
        f1.create_polygon(160, 90, 170, 90, 170, 100, 160, 100, 160, 90, width=1, fill='magenta4')
        f1.create_polygon(170, 90, 180, 90, 180, 100, 170, 100, 170, 90,  width=1, fill='snow')
        f1.create_polygon(140, 100, 160, 100, 160, 110, 140, 110, 140, 100, width=1, fill='chocolate1')
        f1.create_polygon(130, 110,170, 110, 170, 120, 130, 120,  width=1, fill='chocolate3')
        #playera
        f1.create_polygon(70, 130, 130, 130, 130, 140, 140, 140, 140, 150, 160, 150, 160, 140, 170, 140, 170, 130, 230, 130, 230, 170, 190, 170, 190, 250, 180, 250, 180, 240, 170, 240, 170, 230, 110, 230, 110, 170, 70, 170, 70, 130,   width=1, fill='deep sky blue')
        #pantalones
        f1.create_polygon(110, 230, 150, 230, 150, 310, 110, 310, 110, 230,  width=1, fill='magenta4')
        f1.create_polygon(150, 230, 170, 230, 170, 240, 180, 240, 180, 250, 190, 250, 190, 310, 150, 310,150, 230, width=1, fill='magenta4')
        #zapatos
        f1.create_polygon(110, 310, 150, 310, 150, 330, 110, 330, 110, 310, width=1, fill='gray47')
        f1.create_polygon(150, 310, 190, 310, 190, 330, 150, 330, 150, 310, width=1, fill='gray47')


def ocultar(ventana): ventana.destroy()
def ejecutar(f):v0.after(200,f)

b1=Button(v0, text='Abrir ventana con linea', command=lambda:ejecutar(mostrar(1)))
b1.grid(row=1,column=1)


v0.mainloop()