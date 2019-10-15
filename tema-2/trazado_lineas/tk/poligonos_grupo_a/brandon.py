from Tkinter import *

class Brandon:
    def funcion(self, figura):
        vs = Toplevel()
        vs.config(bg="green")
        vs.title(figura)

        panel = Canvas(vs, width=220, height=460, bg="white")
        panel.pack()

        # Sombra
        panel.create_polygon(60, 10, 150, 10, 150, 20, 160, 20, 160, 130, 150, 130, 150, 140, 170, 140, 170, 150,
                             180, 150, 180, 160, 190, 160, 190, 180, 200, 180, 200, 240, 190, 240, 190, 250, 180, 250,
                             180, 260, 170, 260, 170, 280, 160, 280, 160, 340, 170, 340, 170, 400, 180, 400, 180, 410,
                             190, 410, 190, 420, 200, 420, 200, 440, 120, 440, 120, 360, 110, 360, 110, 360, 110, 320,
                             100, 320, 100, 360, 90, 360, 90, 440, 10, 440, 10, 420, 20, 420, 20, 410, 30, 410, 30, 400,
                             40, 400, 40, 340, 50, 340, 50, 280, 40, 280, 40, 260, 30, 260, 30, 250, 20, 250, 20, 240,
                             10, 240, 10, 180, 20, 180, 20, 160, 30, 160, 30, 150, 40, 150, 40, 140, 60, 140, 60, 130,
                             50, 130, 50, 20, 60, 20, width=1, fill="black", outline="black")

        # Cabeza
        panel.create_polygon(60, 20, 150, 20, 150, 30, 140, 30, 140, 40, 70, 40, 70, 30, 60, 30, width=3, fill="white",
                             outline="white")

        # Cara
        panel.create_polygon(60, 40, 70, 40, 70, 50, 140, 50, 140, 40, 150, 40, 150, 130, 140, 130, 140, 140, 70, 140,
                             70, 130, 60, 130, width=1, fill="white", outline="white")
        # Ojos
        panel.create_polygon(70, 70, 80, 70, 80, 80, 90, 80, 90, 70, 100, 70, 100, 80, 90, 80, 90, 90, 100, 90, 100,
                             100,
                             90, 100, 90, 90, 80, 90, 80, 100, 70, 100, 70, 90, 80, 90, 80, 80, 70, 80, 70, 70, width=1,
                             fill="black", outline="black")
        panel.create_polygon(110, 70, 120, 70, 120, 80, 130, 80, 130, 70, 140, 70, 140, 80, 130, 80, 130, 90, 140, 90,
                             140, 100, 130, 100, 130, 90, 120, 90, 120, 100, 110, 100, 110, 90, 120, 90, 120, 80, 110,
                             80, width=1,
                             fill="black", outline="black")

        # Boca
        panel.create_polygon(70, 110, 80, 110, 80, 120, 130, 120, 130, 110, 140, 110, 140, 120, 130, 120, 130, 130, 80,
                             130,
                             80, 120, 70, 120, 70, 110, width=1, fill="black", outline="black")

        # Cuello
        panel.create_polygon(90, 140, 120, 140, 120, 150, 110, 150, 110, 160, 100, 160, 100, 150, 90, 150, width=1,
                             fill="#FFCC99", outline="#FFCC99")
        panel.create_polygon(90, 150, 100, 150, 100, 160, 110, 160, 110, 150, 120, 150, 120, 160, 110, 160, 110, 170,
                             100, 170, 100, 160, 90, 160, 90, 150, width=1, fill="gray", outline="gray")

        # Brazo izquierdo
        panel.create_polygon(40, 150, 60, 150, 60, 160, 70, 160, 70, 190, 80, 190, 80, 200, 60, 200, 60, 190,
                             50, 190, 50, 210, 40, 210, 40, 220, 60, 220, 60, 210, 70, 210, 70, 240, 60, 240, 60, 250,
                             30, 250, 30, 240, 20, 240, 20, 180, 30, 180, 30, 160, 40, 160, 40, 150,
                             width=1, fill="white", outline="white")
        # panel.create_line()

        # Brazo derecho
        panel.create_polygon(130, 200, 130, 190, 140, 190, 140, 160, 150, 160, 150, 150, 170, 150, 170, 160, 180, 160,
                             180, 180, 190, 180, 190, 240, 180, 240, 180, 250, 150, 250, 150, 240, 140, 240, 140, 200,
                             130, 200, width=1, fill="white", outline="white")
        panel.create_polygon(140, 200, 150, 200, 150, 190, 160, 190, 160, 210, 170, 210, 170, 220, 150, 220,
                             150, 210, 140, 210, 140, 200, width=1, fill="black", outline="black")

        # Cuerpo
        panel.create_polygon(80, 150, 90, 150, 90, 160, 100, 160, 100, 170, 110, 170, 110, 160, 120, 160, 120, 210,
                             110, 210, 110, 230, 120, 230, 120, 240, 140, 240, 140, 250, 150, 250, 150, 290, 60, 290,
                             60, 250, 70, 250, 70, 240, 90, 240, 90, 230, 100, 230, 100, 210, 90, 210, 90, 160, 80, 160,
                             80, 250, width=1, fill="white", outline="white")

        # Cinturon
        panel.create_polygon(60, 290, 150, 290, 150, 300, 60, 300, width=1, fill="gray", outline="gray")

        # Mano izquierda
        panel.create_polygon(70, 200, 80, 200, 80, 210, 100, 210, 100, 230, 70, 230, 70, 200, width=1,
                             fill="#FFCC99", outline="#FFCC99")

        # Mano derecha
        panel.create_polygon(110, 210, 130, 210, 130, 200, 140, 200, 140, 230, 110, 230, 110, 210, width=1,
                             fill="#FFCC99", outline="#FFCC99")

        # Pierna Izquierda
        panel.create_polygon(60, 300, 100, 300, 100, 320, 90, 320, 90, 360, 80, 360, 80, 400, 50, 400, 50, 340, 60, 340,
                             60, 300, width=1, fill="white", outline="white")

        # Pierna Derecha
        panel.create_polygon(110, 300, 150, 300, 150, 340, 160, 340, 160, 400, 130, 400, 130, 360, 120, 360, 120, 320,
                             110, 320, width=1, fill="white", outline="white")

        # Pie Izquierdo
        panel.create_polygon(40, 400, 50, 400, 50, 420, 40, 420, width=1, fill="gray", outline="gray")
        panel.create_polygon(30, 410, 40, 410, 40, 420, 50, 420, 50, 410, 80, 410, 80, 430, 20, 430, 20, 420, 30, 420,
                             width=1, fill="white", outline="white")
        panel.create_polygon(60, 410, 70, 410, 70, 420, 60, 420, width=1, fill="gray", outline="gray")

        # Pie Derecho
        panel.create_polygon(160, 400, 170, 400, 170, 420, 160, 420, width=1, fill="gray", outline="gray")
        panel.create_polygon(180, 410, 170, 410, 170, 420, 160, 420, 160, 410, 130, 410, 130, 430, 190, 430, 190, 420,
                             180, 420, width=1, fill="white", outline="white")
        panel.create_polygon(140, 410, 150, 410, 150, 420, 140, 420, width=1, fill="gray", outline="gray")