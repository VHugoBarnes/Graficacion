# coding: utf-8
"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""
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
    elif seleccion == 2:
        panel = Canvas(vs, width=500, height=450, bg="gray")
        panel.pack()
        # cara
        panel.create_polygon(200, 80, 120, 240, 120, 260, 140, 300, 160, 310, 240, 310, 310, 290, 350, 280, 360, 250,
                             350, 230,
                             340, 210, 250, 80,
                             width=1, fill="yellow", outline="black")
        # cejas
        panel.create_polygon(150, 190, 142, 200, 175, 225, 185, 210, width=1, fill="black", outline="black")
        panel.create_polygon(200, 210, 210, 220, 248, 205, 240, 190, width=1, fill="black", outline="black")
        # boca
        panel.create_polygon(150, 250, 150, 260, 185, 255, 170, 263,
                             173, 275, 205, 263, 200, 240, width=2, fill="orange", outline="black")
        # ojos
        panel.create_oval(210, 215, 255, 235, width=1, fill="white", outline="black")
        panel.create_oval(140, 218, 175, 235, width=1, fill="white", outline="black")
        # pupilas
        panel.create_oval(215, 215, 235, 235, width=1, fill="black", outline="black")
        panel.create_oval(140, 218, 160, 235, width=1, fill="black", outline="black")
        # cabello
        panel.create_polygon(200, 80, 210, 75, 210, 60, 220, 50, 220, 70, 230, 50, 240, 50,
                             240, 60, 230, 70, 255, 65, 260, 70, 240, 78,
                             260, 80, 230, 88, width=1, fill="black", outline="black")
    elif seleccion == 3:
        panel = Canvas(vs, width=500, height=450, bg="skyblue")
        panel.pack()
        # cara
        panel.create_oval(120, 80, 320, 200, width=2, fill="chocolate", outline="black")

        # ojos
        panel.create_oval(180, 100, 200, 130, width=1, fill="black", outline="black")
        panel.create_oval(240, 100, 260, 130, width=1, fill="black", outline="black")

        # pupila
        panel.create_oval(185, 105, 190, 115, width=1, fill="white", outline="black")
        panel.create_oval(245, 105, 250, 115, width=1, fill="white", outline="black")

        # boca
        panel.create_arc(170, 140, 270, 180, extent=180, style=CHORD, start=180, width=2, fill="black", outline="black")

        # sonrisa rosybrown
        panel.create_arc(155, 145, 190, 160, extent=100, style=ARC, start=180, width=2, fill="black", outline="black")
        panel.create_arc(255, 145, 290, 160, extent=100, style=ARC, start=255, width=2, fill="black", outline="black")
        panel.create_oval(195, 170, 245, 180, width=2, fill="pink2", outline="black")

        # Petalos
        panel.create_arc(200, 30, 240, 130, extent=180, start=0, style=CHORD, width=2, fill="yellow2", outline="black")
        panel.create_arc(240, 40, 280, 130, extent=180, start=353, style=CHORD, width=2, fill="yellow2",
                         outline="black")
        panel.create_arc(275, 58, 315, 145, extent=185, start=340, style=CHORD, width=2, fill="yellow2",
                         outline="black")
        panel.create_arc(255, 100, 365, 140, extent=190, start=280, style=CHORD, width=2, fill="yellow2",
                         outline="black")
        panel.create_arc(260, 130, 360, 170, extent=180, start=268, style=CHORD, width=2, fill="yellow2",
                         outline="black")
        panel.create_arc(245, 200, 360, 165, extent=220, start=225, style=CHORD, width=2, fill="yellow2",
                         outline="black")
        panel.create_arc(255, 163, 295, 233, extent=215, start=178, style=CHORD, width=2, fill="yellow2",
                         outline="black")
        panel.create_arc(225, 155, 265, 245, extent=190, start=180, style=CHORD, width=2, fill="yellow2",
                         outline="black")
        panel.create_arc(170, 155, 215, 245, extent=190, start=170, style=CHORD, width=2, fill="yellow2",
                         outline="black")
        panel.create_arc(135, 158, 175, 233, extent=210, start=150, style=CHORD, width=2, fill="yellow2",
                         outline="black")
        panel.create_arc(80, 155, 192, 195, extent=198, start=105, style=CHORD, width=2, fill="yellow2",
                         outline="black")
        panel.create_arc(65, 120, 172, 160, extent=193, start=84, style=CHORD, width=2, fill="yellow2", outline="black")

        panel.create_arc(128, 50, 168, 133, extent=200, start=10, style=CHORD, width=2, fill="yellow2", outline="black")

        panel.create_arc(80, 83, 170, 123, extent=233, start=35, style=CHORD, width=2, fill="yellow2", outline="black")
        panel.create_arc(160, 40, 200, 125, extent=190, start=2, style=CHORD, width=2, fill="yellow2", outline="black")

        # tallo
        panel.create_polygon(210, 200, 210, 250, 220, 290, 235, 330, 230, 380, 230, 410,
                             245, 410, 245, 380, 250, 330, 235, 290, 225, 250, 225, 200, width=1, fill="forestgreen",
                             outline="black")
        # hoja derecha
        panel.create_arc(230, 250, 310, 300, extent=270, start=0, style=CHORD, width=2, fill="forestgreen",
                         outline="darkgreen")
        panel.create_arc(230, 265, 300, 295, extent=105, start=75, style=ARC, width=2, outline="darkgreen")
        # hoja izquierda
        panel.create_arc(125, 250, 215, 300, extent=270, start=270, style=CHORD, width=2, fill="forestgreen",
                         outline="darkgreen")
        panel.create_arc(130, 265, 215, 295, extent=105, start=0, style=ARC, width=2, outline="darkgreen")

        # fondo derecho
        panel.create_arc(245, 300, 360, 410, extent=180, start=0, style=CHORD, width=1, fill="darkgreen",
                         outline="black")
        panel.create_arc(245, 325, 380, 440, extent=170, start=0, style=CHORD, width=2, fill="forestgreen",
                         outline="darkgreen")
        panel.create_arc(240, 340, 365, 460, extent=105, start=35, style=ARC, width=2, fill="forestgreen",
                         outline="darkgreen")
        # fondo izquierdo
        panel.create_arc(115, 310, 235, 400, extent=195, start=345, style=CHORD, width=1, fill="darkgreen",
                         outline="black")
        panel.create_arc(105, 340, 235, 470, extent=170, start=20, style=CHORD, width=2, fill="forestgreen",
                         outline="darkgreen")
        panel.create_arc(135, 350, 240, 490, extent=130, style=ARC, start=8, width=2, fill="black", outline="darkgreen")
        # fondo medio
        panel.create_arc(185, 345, 350, 500, extent=180, start=0, style=CHORD, width=2, fill="forestgreen",
                         outline="darkgreen")
        panel.create_arc(185, 365, 315, 500, extent=130, style=ARC, start=40, width=2, outline="darkgreen")
    elif seleccion == 4:
        panel = Canvas(vs, width=600, height=800, bg="linen")
        panel.pack()
        # cara
        panel.create_polygon(200, 300, 200, 450, 210, 470, 390, 470, 400, 450, 400, 300, width=2, fill="lemonchiffon",
                             outline="black")
        # cabeza
        panel.create_arc(100, 80, 500, 520, extent=180, start=0, style=CHORD, width=2, fill="gold", outline="black")
        # manchas

        panel.create_oval(290, 100, 380, 140, width=1, fill="goldenrod", outline="khaki")  # 1
        panel.create_oval(170, 110, 275, 190, width=1, fill="goldenrod", outline="khaki")  # 2
        panel.create_oval(130, 220, 180, 270, width=1, fill="goldenrod", outline="khaki")  # 3
        panel.create_oval(210, 200, 300, 290, width=1, fill="goldenrod", outline="khaki")  # 4
        panel.create_oval(320, 160, 350, 210, width=1, fill="goldenrod", outline="khaki")  # 5
        panel.create_oval(325, 235, 375, 275, width=1, fill="goldenrod", outline="khaki")  # 6
        panel.create_oval(390, 140, 465, 285, width=1, fill="goldenrod", outline="khaki")  # 7

        # ojos
        panel.create_oval(240, 320, 270, 390, width=1, fill="black", outline="black")
        panel.create_oval(330, 320, 360, 390, width=1, fill="black", outline="black")
        # pupila
        panel.create_oval(245, 325, 265, 355, width=1, fill="white", outline="black")
        panel.create_oval(335, 325, 355, 355, width=1, fill="white", outline="black")
        # boca
        panel.create_arc(260, 390, 340, 440, extent=180, style=ARC, start=180, width=2, fill="black", outline="black")
    elif seleccion == 5:
        panel = Canvas(vs, width=1148, height=700, bg='light blue')
        panel.pack()
        # casa
        panel.create_rectangle(100, 410, 370, 650, width=2, fill='yellow', outline='black')
        # tejado
        panel.create_polygon(70, 409, 400, 409, 245, 200, width=2, fill='red', outline='black')
        # ventanas
        panel.create_rectangle(120, 420, 200, 500, width=2, fill='blue', outline='black')
        panel.create_rectangle(270, 420, 350, 500, width=2, fill='purple', outline='black')
        # Puerta
        panel.create_rectangle(200, 550, 260, 650, width=2, fill='red', outline='black')
        panel.create_line(230, 550, 230, 650, width=2, fill="black")
        panel.create_oval(215, 600, 200, 620, width=2, fill='brown', outline='black')
        # pasto
        panel.create_rectangle(1, 650, 1147, 700, width=2, fill='green', outline='black')
        # arbol
        panel.create_rectangle(600, 410, 570, 650, width=2, fill='brown', outline='black')
        panel.create_oval(700, 550, 480, 350, width=2, fill='green', outline='black')
        # sol
        panel.create_oval(1000, 150, 880, 50, width=2, fill='yellow', outline='black')
        panel.create_line(900, 200, 1000, 1, width=10, fill="yellow")
        panel.create_line(780, 125, 1100, 70, width=10, fill="yellow")
        panel.create_line(1050, 200, 880, 10, width=10, fill="yellow")
    elif seleccion == 6:
        panel = Canvas(vs, width=200, height=200, bg="gray")
        panel.pack()

        # Primera parte negra
        panel.create_polygon(70, 50, 70, 60, 50, 60, 50, 70, 40, 70, 40, 150, 50, 150, 50, 160, 60, 160, 60, 170, 80,
                             170, 80, 180,
                             110, 180, 110, 170, 130, 170, 130, 160, 140, 160, 140, 150, 150, 150, 150, 70,
                             140, 70, 140, 60, 120, 60, 120, 50, 70, 50, width=1, fill="black")

        # ojo 1
        panel.create_polygon(50, 80, 50, 120, 60, 120, 60, 130, 80, 130, 80, 120, 90, 120, 90, 110, 80, 110, 80, 100,
                             70, 100, 70, 90
                             , 60, 90, 60, 80, 50, 80, width=1, fill="white")

        # ojo 2
        panel.create_polygon(140, 80, 130, 80, 130, 90, 120, 90, 120, 100, 110, 100, 110, 110, 100, 110, 100, 120, 110,
                             130, 130, 130, 130, 120
                             , 140, 120, 140, 80, 130, 80, width=1, fill="white")
    elif seleccion == 7:
        panel = Canvas(vs, width=200, height=200, bg="yellow")
        panel.pack()
        # Parte negra
        panel.create_polygon(70, 10, 130, 10, 130, 20, 150, 20, 150, 30, 160, 30, 160, 50, 170, 50, 170, 60, 180, 60,
                             180, 130,
                             170, 130, 170, 140, 160, 140, 160, 160, 150, 160, 150, 170, 50, 170, 50, 160, 40, 160, 40,
                             140, 30, 140, 30, 130, 20, 130,
                             20, 60, 30, 60, 30, 50, 40, 50, 40, 30, 50, 30, 50, 20, 70, 20, 70, 10, width=1,
                             fill="black", outline="black")

        # Primera parte blanca
        panel.create_polygon(80, 20, 120, 20, 120, 30, 140, 30, 140, 40, 150, 40, 150, 60, 160, 60, 160, 70, 170, 70,
                             170, 120, 150, 120, 150, 110, 50, 110, 50, 120, 30, 120, 30, 70, 40, 70, 40, 60, 50, 60,
                             50, 40, 60, 40, 60, 30, 80, 30, 80, 20, width=1, fill="white", outline="white")

        # segunda parte blanca
        panel.create_polygon(60, 120, 140, 120, 140, 130, 150, 130, 150, 150, 140, 150, 140, 160, 60, 160, 60, 150,
                             50, 150, 50, 130, 60, 130, 60, 120, width=1, fill="white", outline="white")

        # ojos
        panel.create_rectangle(80, 120, 90, 140, width=1, fill="black", outline="black")
        panel.create_rectangle(110, 120, 120, 140, width=1, fill="black", outline="black")

        # manchas
        panel.create_polygon(80, 70, 120, 70, 120, 80, 130, 80, 130, 100, 120, 100, 120, 110, 80, 110, 80, 100, 70, 100,
                             70, 80, 80, 80, 80, 70, width=1, fill="red", outline="red")
        panel.create_polygon(110, 20, 120, 20, 120, 30, 140, 30, 140, 50, 120, 50, 120, 40, 110, 40, 110, 20, width=1,
                             fill="red", outline="red")
        panel.create_polygon(80, 20, 90, 20, 90, 40, 80, 40, 80, 50, 60, 50, 60, 30, 80, 30, 80, 20, width=1,
                             fill="red", outline="red")
        panel.create_polygon(40, 60, 60, 60, 60, 90, 50, 90, 50, 100, 30, 100, 30, 70, 40, 70, 40, 60, width=1,
                             fill="red", outline="red")
        panel.create_polygon(140, 60, 160, 60, 160, 70, 170, 70, 170, 100, 150, 100, 150, 90, 140, 90, 140, 60, width=1,
                             fill="red", outline="red")
    elif seleccion == 8:
        panel = Canvas(vs, width=400, height=400, bg='red')
        panel.pack()
        panel.create_polygon(60, 120, 100, 180, 140, 120, 100, 60, width=5, fill='blue',
                             outline='green')  # coordenadas de x1,y1,x2,y2 etc etc y caracteristicas de las figura
    elif seleccion == 9:
        canvas = Canvas(vs, width=500, height=500, bg="white")
        canvas.pack()

        canvas.create_polygon(42, 372, 9, 396, -5, 415, -5, 502, 505, 505, 505, 396, 453, 372,
                              fill="BLUE", outline="black", width=2)
        canvas.create_polygon(177, 261, 173, 293, 174, 323, 179, 329, 174, 323, 174, 312, 140, 323, 124, 335, 150, 420,
                              346, 435, 383, 341, 363, 324, 326, 312, 327, 312, 319, 340, 327, 312, 323, 268,
                              fill="peach puff", outline="black", width=2)
        canvas.create_polygon(119, 337, 157, 340, 183, 356, 198, 382, 110, 381,
                              fill="peach puff", outline="black", width=2)
        canvas.create_polygon(365, 337, 325, 340, 301, 356, 282, 382, 367, 381,
                              fill="peach puff", outline="black", width=2)
        canvas.create_polygon(137, 365, 181, 363, 229, 369, 249, 382, 252, 403, 249, 382, 260, 373, 297, 365, 362, 367,
                              368, 482, 98, 482,
                              fill="peach puff", outline="black", width=2)
        canvas.create_polygon(114, 353, 212, 399, 269, 401, 369, 355, 350, 484, 127, 482,
                              fill="blue", outline="black", width=2)
        canvas.create_polygon(138, 325, 119, 319, 136, 373, 183, 422, 237, 460, 267, 457, 335, 399, 367, 331, 369, 313,
                              361, 319, 369, 313, 440, 347, 433, 382, 439, 353,
                              474, 372, 431, 502, 85, 502, 32, 374, 68, 357, 75, 375,
                              67, 357, 68, 346, 119, 319,
                              fill="orange", outline="black", width=2)

        canvas.create_polygon(196, 306, 215, 334, 230, 353, 215, 334,
                              fill="peach puff", outline="black", width=2)
        canvas.create_polygon(304, 306, 289, 334, 270, 353, 289, 334,
                              fill="peach puff", outline="black", width=2)
        canvas.create_polygon(184, 260, 117, 276, 80, 305, 106, 254, 127, 233, 79, 232, 44, 249, 71, 203, 112, 184, 82,
                              165, 24, 165, 84, 125, 144, 108, 134, 55, 91, 1, 206, 43, 240, 89, 268, 88,
                              311, 103, 336, 130, 372, 132, 423, 170, 396, 170, 374, 177, 403, 203, 419, 232, 400, 224,
                              376, 224, 398, 246, 376, 241, 334, 243, 344, 239, 353, 250, 364, 271, 342, 261, 323, 260

                              )
        canvas.create_oval(340, 445, 390, 495, fill="white", outline="black", width=2)
        canvas.create_polygon(180, 260,
                              155, 244,
                              143, 208,
                              155, 193,
                              165, 195, fill="peach puff", outline="black", width=2)

        canvas.create_polygon(320, 260,
                              345, 244,
                              357, 208,
                              345, 193,
                              335, 195, fill="peach puff", outline="black", width=2)

        canvas.create_polygon(240, 325,
                              180, 275,
                              160, 170,
                              330, 170,
                              340, 190,
                              320, 275,
                              260, 325, fill="peach puff", outline="black", width=2)

        canvas.create_polygon(250, 255,
                              250, 275,
                              260, 275,
                              250, 280,
                              240, 275, fill="peach puff3", outline="black", width=2)

        canvas.create_polygon(235, 290,
                              260, 287,
                              265, 290,
                              260, 287, outline="black", width=2)

        canvas.create_polygon(237, 247,
                              233, 253,
                              200, 245,
                              190, 195, fill="white", outline="black", width=2)
        canvas.create_oval(210, 223.5,
                           230, 243, fill="black")
        canvas.create_polygon(240, 250,
                              242, 235,
                              242, 243,
                              180, 180,
                              180, 200,
                              fill="black", outline="black", width=2)

        canvas.create_polygon(263, 247,
                              267, 253,
                              300, 245,
                              310, 195, fill="white", outline="black", width=2)

        canvas.create_oval(290, 223.5,
                           270, 243, fill="black")

        canvas.create_polygon(260, 250,
                              257, 235,
                              258, 243,
                              320, 180,
                              320, 200,
                              fill="black", outline="black", width=2)

        canvas.create_polygon(280, 160,
                              240, 220,
                              225, 265,
                              215, 180,
                              220, 160,
                              223, 183,
                              190, 200,
                              170, 250,
                              155, 170,
                              210, 160)

        canvas.create_polygon(266, 174,
                              296, 206, 311, 245, 321, 204, 313, 156, 256, 121, 220, 174)
        canvas.create_polygon(313, 184, 327, 200, 332, 226, 342, 198, 331, 149, 305, 128, 256, 125)

    elif seleccion == 10:
        poligono = Canvas(vs, width=400, height=400, bg="gray")
        poligono.create_polygon(130, 20, 60, 80, 100, 140, 160, 140, 200, 80, width=3, fill="pink", outline="black")
        poligono.pack()

    elif seleccion == 11:
        panel = Canvas(vs, width=500, height=400, bg='white')
        panel.pack()
        panel.create_polygon(140, 40, 300, 40, 400, 140, 40, 140, width=5, fill='white', outline='black')
        # coordenadas y caracteristica de la figura


    elif seleccion == 12:
        panel = Canvas(vs, width=225, height=200, bg="white")
        panel.pack()
        # Parte negra
        panel.create_polygon(70, 10, 170, 10, 170, 20, 190, 20, 190, 30, 200, 30, 200, 80, 190, 80, 190, 90, 170, 90,
                             170, 100, 140, 100, 140, 120, 150, 120, 150, 110, 170, 110, 170, 100, 190, 100, 190, 110,
                             200, 110, 200, 140, 190, 140, 190, 150, 180, 150, 180, 160, 160, 160, 160, 170, 80, 170,
                             80, 160, 60, 160, 60, 150, 50, 150, 50, 140, 40, 140, 40, 110, 50, 110, 50, 100, 70, 100,
                             70, 110, 90, 110, 90, 120, 100, 120, 100, 100, 70, 100, 70, 90, 50, 90, 50, 80, 40, 80, 40,
                             30, 50, 30, 50, 20, 70, 20, 70, 10, width=1, fill="black", outline="black")

        # Parte naranja
        panel.create_polygon(80, 20, 160, 20, 160, 30, 180, 30, 180, 40, 190, 40, 190, 70, 180, 70, 180, 80, 160, 80,
                             160, 90, 80, 90, 80, 80, 60, 80, 60, 70, 50, 70, 50, 40, 60, 40, 60, 30, 80, 30, 80, 20,
                             width=1, fill="orange", outline="orange")

        # Parte amarilla
        panel.create_polygon(90, 30, 150, 30, 150, 40, 170, 40, 170, 70, 150, 70, 150, 80, 90, 80, 90, 70, 70, 70, 70,
                             40, 90, 40, 90, 30, width=1, fill="yellow", outline="yellow")

        # Parte blanca
        panel.create_polygon(90, 50, 150, 50, 150, 60, 90, 60, 90, 50, width=1, fill="white", outline="white")

        # Ojos rectangulos negros
        panel.create_rectangle(100, 40, 110, 70, width=1, fill="black", outline="black")
        panel.create_rectangle(130, 40, 140, 70, width=1, fill="black", outline="black")

        # Parte verde
        panel.create_polygon(110, 100, 130, 100, 130, 150, 140, 150, 140, 130, 150, 130, 150, 120, 170, 120, 170, 110,
                             190, 110, 190, 140, 180, 140, 180, 150, 160, 150, 160, 160, 80, 160, 80, 150, 60, 150, 60,
                             140, 50, 140, 50, 110, 70, 110, 70, 120, 90, 120, 90, 130, 100, 130, 100, 150, 110, 150,
                             110, 100, width=1, fill="green", outline="green")

    elif seleccion == 13:
        panel = Canvas(vs, width=300, height=200, bg="black")
        panel.pack()

        # Cuerpo del fantasma
        panel.create_polygon(100, 10, 130, 10, 130, 20, 150, 20, 150, 20, 150, 30, 160, 30, 160, 40, 170, 40, 170, 60,
                             180, 60, 180, 160, 170, 160,
                             170, 150, 160, 150, 160, 140, 150, 140, 150, 150, 140, 150, 140, 160, 130, 160, 130, 140,
                             100, 140, 100, 160,
                             90, 160, 90, 150, 80, 150, 80, 140, 70, 140, 70, 150, 60, 150, 60, 160, 50, 160, 50, 60,
                             60, 60,
                             60, 40, 70, 40, 70, 30, 80, 30, 80, 20, 100, 20, width=1, fill="blue", outline="white")

        # Ojos Fantasma
        panel.create_polygon(80, 50, 100, 50, 100, 70, 80, 70, width=1, fill="white")
        panel.create_polygon(130, 50, 150, 50, 150, 70, 130, 70, width=1, fill="white")

        # Boca Fantasma
        panel.create_polygon(65, 110, 70, 110, 70, 120, 65, 120, width=1, fill="white")
        panel.create_polygon(70, 100, 90, 100, 90, 110, 70, 110, width=1, fill="white")
        panel.create_polygon(90, 110, 110, 110, 110, 120, 90, 120, width=1, fill="white")
        panel.create_polygon(110, 100, 130, 100, 130, 110, 110, 110, width=1, fill="white")
        panel.create_polygon(130, 110, 150, 110, 150, 120, 130, 120, width=1, fill="white")
        panel.create_polygon(150, 100, 170, 100, 170, 110, 150, 110, width=1, fill="white")
        panel.create_polygon(170, 110, 175, 110, 175, 120, 170, 120, width=1, fill="white")

    elif seleccion == 14:
        Escudo = Canvas(vs, width=420, height=420, bg='blue')
        # Primer Arco Rojo
        Escudo.create_oval(40, 40, 400, 400, width=7, fill='red')
        # Arco Gris
        Escudo.create_oval(90, 90, 350, 350, width=7, fill='grey')
        # Segundo Arco Rojo
        Escudo.create_oval(140, 140, 302, 302, width=7, fill='red')
        # Arco Azul
        Escudo.create_oval(163, 163, 278, 278, width=7, fill='blue')
        # Estrella Blanca
        Escudo.create_polygon(222, 170,
                              250, 268,
                              170, 200,
                              270, 200,
                              185, 268, width=5, fill="white", outline="white")

        Escudo.pack()  # para que pueda aparecer el Escudo

    elif seleccion == 15:
        circulo = Canvas(vs, width=210, height=210, bg='magenta')
        circulo.pack()
        circulo.create_oval(20, 20, 200, 200, width=10, fill='yellow')
        circulo.create_oval(90, 92, 70, 70, width=10, fill='black')
        circulo.create_oval(140, 70, 160, 92, width=10, fill='black')
        circulo.create_oval(140, 155, 90, 110, width=10, fill='black')

    elif seleccion == 16:
        dib = Canvas(vs, width=800, height=800, bg="cyan")
        dib.pack(expand=YES, fill=BOTH)
        # gorra
        dib.create_polygon(250, 0, 250, 50, 200, 50, 200, 100, 650, 100, 650, 50, 500, 50, 500, 0, width=1, fill="red",
                           outline="black")
        # cabelloenJota
        dib.create_polygon(200, 100, 200, 150, 250, 150, 250, 250, 350, 250, 350, 200, 300, 200, 300, 150, 350, 150,
                           350, 100, width=1, fill="brown", outline="black")
        # oreja
        dib.create_polygon(200, 150, 200, 250, 250, 250, 250, 150, width=1, fill="yellow", outline="black")
        # cabellodetrasoreja
        dib.create_polygon(200, 150, 150, 150, 150, 250, 200, 250, 200, 150, width=1, fill="brown", outline="black")
        # cabellobajooreja
        dib.create_polygon(200, 250, 200, 300, 250, 300, 250, 250, width=1, fill="brown", outline="black")
        # cara
        dib.create_polygon(350, 100, 350, 150, 300, 150, 300, 200, 350, 200, 350, 250, 250, 250, 250, 350, 550, 350,
                           550, 250, 700, 250, 700, 200, 650, 200, 650, 150, 550, 150, 550, 100, 350, 100, width=1,
                           fill="yellow", outline="black")
        # ojo
        dib.create_polygon(450, 100, 450, 200, 500, 200, 500, 100)
        # Mostacho
        dib.create_polygon(500, 200, 500, 250, 450, 250, 450, 300, 650, 300, 650, 250, 550, 250, 550, 200)
        # Mangaizquierda
        dib.create_polygon(300, 350, 200, 350, 200, 400, 150, 400, 150, 450, 100, 450, 100, 500, 200, 500, 200, 550,
                           250, 550, 250, 500, 300, 500, 300, 350, width=1, fill="red", outline="black")
        # centro
        dib.create_polygon(350, 350, 350, 450, 450, 450, 450, 350, width=1, fill="red", outline="black")
        # Mangaderecha
        dib.create_polygon(500, 350, 500, 500, 550, 500, 550, 550, 600, 550, 600, 500, 700, 500, 700, 450, 650, 450,
                           650, 400, 600, 400, 600, 350, width=1, fill="red", outline="black")
        # Manoizquierda
        dib.create_polygon(100, 500, 100, 650, 200, 650, 200, 600, 250, 600, 250, 550, 200, 550, 200, 500, width=1,
                           fill="yellow", outline="black")
        # Manoderecha
        dib.create_polygon(600, 500, 600, 550, 550, 550, 550, 600, 600, 600, 600, 650, 700, 650, 700, 500, width=1,
                           fill="yellow", outline="black")
        # ropita
        dib.create_polygon(300, 350, 300, 500, 250, 500, 250, 600, 200, 600, 200, 700, 350, 700, 350, 650, 450, 650,
                           450, 700, 600, 700, 600, 600, 550, 600, 550, 500, 500, 500, 500, 350, 450, 350, 450, 450,
                           350, 450, 350, 350, width=1, fill="blue", outline="black")
        # botonizquierdo
        dib.create_polygon(300, 500, 300, 550, 350, 550, 350, 500, width=1, fill="yellow", outline="black")
        # botonderecho
        dib.create_polygon(450, 500, 450, 550, 500, 550, 500, 500, width=1, fill="yellow", outline="black")
        # botaizquierda
        dib.create_polygon(150, 700, 150, 750, 100, 750, 100, 800, 300, 800, 300, 700, width=1, fill="brown",
                           outline="black")
        # botaderecha
        dib.create_polygon(500, 700, 500, 800, 700, 800, 700, 750, 650, 750, 650, 700, width=1, fill="brown",
                           outline="black")

    elif seleccion == 17:
        bat = Canvas(vs, width=280, height=280, bg="blue")
        bat.pack(expand=YES, fill=BOTH)
        # Mascara
        bat.create_polygon(80, 20, 60, 20, 60, 160, 80, 160, 80, 180, 180, 180, 180, 160, 200, 160, 200, 20, 180, 20,
                           180, 40, 160, 40, 160, 60, 100, 60, 100, 40, 80, 40, 80, 20)
        # ojoizquierdo
        bat.create_polygon(100, 100, 100, 120, 120, 120, 120, 100, width=1, fill="white", outline="black")
        # ojoderecho
        bat.create_polygon(140, 100, 140, 120, 160, 120, 160, 100, width=1, fill="white", outline="black")
        # boca
        bat.create_polygon(80, 140, 80, 160, 180, 160, 180, 140, width=1, fill="pink", outline="black")
        # brazos
        bat.create_polygon(80, 160, 40, 160, 40, 200, 220, 200, 220, 160, 180, 160, 180, 180, 80, 180, width=1,
                           fill="gray", outline="black")
        # capa
        bat.create_polygon(60, 200, 60, 260, 80, 260, 80, 220, 180, 220, 180, 260, 200, 260, 200, 200)
        # cinturon
        bat.create_polygon(120, 200, 120, 220, 140, 220, 140, 200, width=1, fill="yellow", outline="black")
        # piernas
        bat.create_polygon(80, 220, 80, 260, 120, 260, 120, 240, 140, 240, 140, 260, 180, 260, 180, 220, width=1,
                           fill="gray", outline="black")
        # restocapa
        bat.create_polygon(120, 240, 120, 260, 140, 260, 140, 240)

    elif seleccion == 18:
        Space = Canvas(vs, width=800, height=500, bg="RED")
        Space.pack(expand=YES, fill=BOTH)

        Space.create_polygon(250, 50, 200, 50, 200, 100, 250, 100, 250, 150, 200, 150, 200, 200, 150, 200, 150, 250,
                             100, 250, 100, 400, 150, 400,
                             150, 300, 200, 300, 200, 450, 350, 450, 350, 400, 250, 400, 250, 350, 500, 350, 500, 400,
                             400, 400, 400, 450, 550, 450, 550, 300, 600, 300, 600, 400,
                             650, 400, 650, 250, 600, 250, 600, 200, 550, 200, 550, 150, 500, 150, 500, 100, 550, 100,
                             550, 50, 450, 50, 450, 150, 300, 150, 300, 50, fill="green", outline="blue", width=6)

        Space.create_polygon(250, 200, 250, 250, 300, 250, 300, 200, fill="white", outline="white", width=6)

        Space.create_polygon(500, 200, 450, 200, 450, 250, 500, 250, fill="white", outline="white", width=6)

    elif seleccion == 19:
        canvas = Canvas(vs, width=500, height=800, bg="White")
        canvas.pack()

        canvas.create_arc(100, 100, 400, 400, start=0, extent=180, fill="green", outline="green")
        canvas.create_oval(175, 150, 200, 175, fill="white", outline="white")
        canvas.create_oval(300, 150, 325, 175, fill="white", outline="white")
        canvas.create_oval(100, 550, 200, 450, fill="green", outline="green")
        canvas.create_polygon(100, 260, 100, 500, 150, 550, 350, 550, 400, 500, 400, 260, fill="green", outline="green")
        canvas.create_oval(300, 550, 400, 450, fill="green", outline="green")
        canvas.create_polygon(160, 550, 160, 625, 220, 625, 220, 550, fill="green", outline="green")
        canvas.create_polygon(280, 550, 280, 625, 340, 625, 340, 550, fill="green", outline="green")
        canvas.create_oval(160, 600, 220, 650, fill="green", outline="green")
        canvas.create_oval(280, 600, 340, 650, fill="green", outline="green")
        canvas.create_polygon(30, 275, 30, 450, 90, 450, 90, 275, fill="green", outline="green")
        canvas.create_oval(30, 250, 90, 300, fill="green", outline="green")
        canvas.create_oval(30, 425, 90, 475, fill="green", outline="green")

        canvas.create_polygon(410, 275, 410, 450, 470, 450, 470, 275, fill="green", outline="green")
        canvas.create_oval(410, 250, 470, 300, fill="green", outline="green")
        canvas.create_oval(410, 425, 470, 475, fill="green", outline="green")

        canvas.create_polygon(160, 130,
                              180, 118,
                              160, 88,
                              140, 100, fill="green", outline="green")
        canvas.create_oval(141, 85, 163, 110, fill="green", outline="green")

        canvas.create_polygon(335, 130,
                              315, 118,
                              335, 88,
                              355, 100, fill="green", outline="green")
        canvas.create_oval(354, 85, 332, 110, fill="green", outline="green")


def funcion_main():
    vp = Tk()
    vp.geometry("300x800+5+5")
    vp.configure(bg="black")
    vp.title("Poligonos grupo A")
    boton1 = Button(vp, text="Perrito", bg="blue", fg="White",
                    command=lambda: funcion(1, "Programa por Ambrocio Laureano"))
    boton1.pack(padx=5, pady=5, fill=X)
    boton2 = Button(vp, text="Angry Bird", bg="blue", fg="White",
                    command=lambda: funcion(2, "Programa por Griselda Maldonado"))
    boton2.pack(padx=5, pady=5, fill=X)
    boton3 = Button(vp, text="Girasol", bg="blue", fg="White",
                    command=lambda: funcion(3, "Programa por Griselda Maldonado"))
    boton3.pack(padx=5, pady=5, fill=X)
    boton4 = Button(vp, text="Hongo", bg="blue", fg="White",
                    command=lambda: funcion(4, "Programa por Griselda Maldonado"))
    boton4.pack(padx=5, pady=5, fill=X)
    boton5 = Button(vp, text="Paisaje", bg="blue", fg="White",
                    command=lambda: funcion(5, "Programa por Manuel Ramirez"))
    boton5.pack(padx=5, pady=5, fill=X)
    boton6 = Button(vp, text="Venom", bg="blue", fg="White",
                    command=lambda: funcion(6, "Programa por Livan Sanchez"))
    boton6.pack(padx=5, pady=5, fill=X)
    boton7 = Button(vp, text="Seta", bg="blue", fg="White",
                    command=lambda: funcion(7, "Programa por Carolina Sauceda"))
    boton7.pack(padx=5, pady=5, fill=X)
    boton8 = Button(vp, text="Rombo", bg="blue", fg="White",
                    command=lambda: funcion(8, "Programa por Carlos Olvera"))
    boton8.pack(padx=5, pady=5, fill=X)
    boton9 = Button(vp, text="Goku", bg="blue", fg="White",
                    command=lambda: funcion(9, "Programa por Santiago Lopez"))
    boton9.pack(padx=5, pady=5, fill=X)
    boton10 = Button(vp, text="Pentagono", bg="blue", fg="White",
                     command=lambda: funcion(10, "Programa por Alondra Adamary"))
    boton10.pack(padx=5, pady=5, fill=X)
    boton11 = Button(vp, text="Cuadrilatero", bg="blue", fg="White",
                     command=lambda: funcion(11, "Programa por Rocio Mahe"))
    boton11.pack(padx=5, pady=5, fill=X)
    boton12 = Button(vp, text="Flor", bg="blue", fg="White",
                     command=lambda: funcion(12, "Programa por Lyvan Lumbreras"))
    boton12.pack(padx=5, pady=5, fill=X)
    boton13 = Button(vp, text="Fantasma", bg="blue", fg="White",
                     command=lambda: funcion(13, "Programa por Fernando Veliz"))
    boton13.pack(padx=5, pady=5, fill=X)
    boton14 = Button(vp, text="Escudo", bg="blue", fg="White",
                     command=lambda: funcion(14, "Programa por Jesus Uribe"))
    boton14.pack(padx=5, pady=5, fill=X)
    boton15 = Button(vp, text="Carita", bg="blue", fg="White",
                     command=lambda: funcion(15, "Programa por Diana Lucia"))
    boton15.pack(padx=5, pady=5, fill=X)
    boton16 = Button(vp, text="Mario Bros", bg="blue", fg="White",
                     command=lambda: funcion(16, "Programa por Alejandro Echavarria"))
    boton16.pack(padx=5, pady=5, fill=X)
    boton17 = Button(vp, text="Batman", bg="blue", fg="White",
                     command=lambda: funcion(17, "Programa por Alejandro Echavarria"))
    boton17.pack(padx=5, pady=5, fill=X)
    boton18 = Button(vp, text="Arcade", bg="blue", fg="White",
                     command=lambda: funcion(18, "Programa por Jaziel Martinez"))
    boton18.pack(padx=5, pady=5, fill=X)
    boton19 = Button(vp, text="Android", bg="blue", fg="White",
                     command=lambda: funcion(19, "Programa por Ivan Gutierrez"))
    boton19.pack(padx=5, pady=5, fill=X)

    vp.mainloop()


funcion_main()

