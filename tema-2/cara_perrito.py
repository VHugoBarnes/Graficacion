from Tkinter import *


def funcion(seleccion, figura):
    vs = Toplevel()
    vs.configure(bg="gray")
    vs.title(figura)
    if seleccion == 1:
        panel = Canvas(vs, width=1200, height=650, bg="gray")
        panel.pack()
        # cara
        panel.create_polygon(415, 50, 235, 490, 365, 625, 755, 625, 850, 500, 700, 50,
                             width=1, fill="#e0af77", outline="brown")
        # orejas
        panel.create_polygon(415, 50, 60, 320, 175, 635, width=1, fill="#bb6400", outline="#000000")
        panel.create_polygon(700, 50, 1045, 320, 896, 635, width=1, fill="#bb6400", outline="#000000")
        # menton
        panel.create_polygon(365, 625, 550, 415, 755, 625, width=1, fill="#bb6400", outline="#000000")
        # ojos
        panel.create_oval(420, 225, 480, 305, width=1, fill="#1a1200", outline="#000000")
        panel.create_oval(630, 225, 690, 305, width=1, fill="#1a1200", outline="#000000")
        # bigotes
        panel.create_oval(475, 525, 490, 540, width=1, fill="#1a1200", outline="#000000")
        panel.create_oval(615, 525, 630, 540, width=1, fill="#1a1200", outline="#000000")
        panel.create_oval(445, 560, 460, 575, width=1, fill="#1a1200", outline="#000000")
        panel.create_oval(610, 560, 625, 575, width=1, fill="#1a1200", outline="#000000")
        panel.create_oval(480, 560, 495, 575, width=1, fill="#1a1200", outline="#000000")
        panel.create_oval(640, 560, 655, 575, width=1, fill="#1a1200", outline="#000000")
        # nariz
        panel.create_oval(470, 305, 640, 500, width=1, fill="#1a1200", outline="#000000")

        boton1 = Button(vs, text='Cerrar', bg='Red', command=lambda: ocultar(vs))
        boton1.pack()


def ocultar (ventana): ventana.withdraw()


vp = Tk()
vp.geometry("300x800+5+5")
vp.configure(bg="black")
vp.title("Poligono cara perrito")

# Hacer boton
boton1 = Button(vp, text="Perrito", bg="blue", fg="White", command=lambda: funcion(1, "Programa por Ambrocio Laureano"))
boton1.pack(padx=5, pady=5, fill=X)

vp.mainloop()