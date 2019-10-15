#By: Kenneth Marlon Barragan Lopez
from Tkinter import *

class Kenneth:
    def funcion(self, figura):
        vs = Toplevel()
        vs.configure(bg="gray")
        vs.title(figura)

        panel = Canvas(vs, width=640, height=180, bg="gray")
        panel.pack()
        # BODY
        panel.create_polygon(50, 10, 70, 10, 70, 30, 90, 30, 90, 50, 150, 50, 150, 30, 170, 30, 190, 30, 190, 10,
                             170, 10, 170, 50, 190, 50, 190, 70, 210, 70, 210, 90, 230, 90, 230, 150, 210, 150,
                             210, 110, 190, 110, 190, 150, 170, 150, 130, 150, 130, 170, 170, 170, 170, 130,
                             70, 130, 70, 150, 70, 170, 110, 170, 110, 150, 50, 150, 50, 110, 30, 110, 30, 150,
                             10, 150, 10, 90, 30, 90, 30, 70, 50, 70, 50, 50, 70, 50, 70, 30, 50, 30, 50, 10,
                             width=1, fill="green", outline="black")
        # OJO
        panel.create_polygon(70, 70, 90, 70, 90, 110, 70, 110, 70, 70,
                             width=1, fill="white", outline="black")
        # OJO
        panel.create_polygon(150, 70, 170, 70, 170, 110, 150, 110, 150, 70,
                             width=1, fill="white", outline="black")
        # Nave
        panel.create_polygon(340, 160, 340, 140, 320, 140, 320, 120, 260, 120, 260, 100, 300, 100, 300, 80, 320,
                             80, 320, 60, 340, 60, 340, 40, 380, 40, 380, 20, 500, 20, 500, 40, 540, 40, 540, 60,
                             560, 60, 560, 80, 580, 80, 580, 100, 620, 100, 620, 120, 560, 120, 560, 140, 540, 140,
                             540, 160, 520, 160, 520, 140, 500, 140, 500, 120, 460, 120, 460, 140, 420, 140, 420, 120,
                             380, 120, 380, 140, 360, 140, 360, 160, 340, 160,
                             width=1, fill="orange", outline="black")
        # NaveWindow
        panel.create_polygon(340, 80, 340, 100, 360, 100, 360, 80, 340, 80,
                             width=1, fill="white", outline="black")
        panel.create_polygon(400, 100, 400, 80, 420, 80, 420, 100, 400, 100,
                             width=1, fill="white", outline="black")
        panel.create_polygon(460, 100, 460, 80, 480, 80, 480, 100, 460, 100,
                             width=1, fill="white", outline="black")
        panel.create_polygon(520, 100, 520, 80, 540, 80, 540, 100, 520, 100,
                             width=1, fill="white", outline="black")