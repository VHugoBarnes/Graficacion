"""
    Programa escrito por: Erick Alexis
"""
from Tkinter import*

class ErickAlexis:

    def mostrar(self, titulo):
        v1 = Toplevel()
        v1.title(titulo)
        v1.protocol('wn_DELETE_WINDOW', "onexit")
        v1.geometry("700x630")
        canvas1 = Canvas(v1, width=800, height=800, bg="#092A81")
        canvas1.pack(expand=YES, fill=BOTH)
        # casco
        canvas1.create_polygon(66, 145, 75, 110, 105, 70, 132, 42, 165, 32, 240, 31, 300, 83, 325, 157, 294, 210,
                               211, 265, 169, 268, 128, 254, 80, 205, width=10, fill='grey', outline="black")
        # VidrioCasco
        canvas1.create_polygon(66, 145, 75, 110, 105, 70, 160, 47, 224, 48, 256, 64, 290, 98, 308, 137, 309, 163, 283,
                               178, 256, 211,
                               211, 265, 169, 268, 128, 254, 80, 205, width=10, fill="black")
        # Cuerpo
        canvas1.create_polygon(294, 210, 211, 265, 169, 268, 165, 275, 175, 320, 220, 375, 310, 420, 410, 430, 430, 440,
                               485, 419, 510, 445,
                               530, 430, 528, 380, 470, 380, 410, 340, 315, 215, width=10, fill='#FFA107',
                               outline="black")
        # LineaPiernas
        canvas1.create_polygon(410, 430, 330, 380, width=10, fill='black', outline="black")

        # Mochila1
        canvas1.create_polygon(315, 215, 410, 340, 470, 295, 435, 210, 380, 180, 360, 180, width=10, fill='#DC5700',
                               outline="black")

        # Mochila2
        canvas1.create_polygon(315, 215, 360, 180, 285, 50, 270, 58, 300, 83, 325, 157, 294, 210, width=10,
                               fill='#CA5101', outline="black")
        # Luna

        # luna
        canvas1.create_oval(-50, 800, 800, 460, width=10, fill='grey')

        # Brazo
        canvas1.create_polygon(165, 275, 155, 318, 115, 340, 109, 350, 118, 370, 135, 380, 160, 370, 193, 350, 175, 320,
                               width=10, fill='black')
        # Palo de bandera
        canvas1.create_polygon(30, 220, 240, 500, width=10, fill='blue', outline="black")
        canvas1.create_polygon(370, 235, 360, 100, width=10, fill='blue', outline="white")
        canvas1.create_polygon(360, 100, width=10, fill='blue', outline="black")

        # bandera
        canvas1.create_polygon(30, 220, 0, 240, 0, 400, 105, 320, width=10, fill='white', outline="black")

        # brazo2
        canvas1.create_polygon(270, 250, 285, 245, 300, 250, 310, 270, 280, 360, 220, 400, 202, 395, 198, 368, 238, 338,
                               width=10, fill='black', outline="black")
        # bota
        canvas1.create_polygon(505, 380, 485, 419, 510, 445,
                               530, 430, 520, 380, width=10, fill='black', outline="black")
        # Reflejo
        canvas1.create_polygon(220, 75, 210, 90, 200, 95, 220, 110, 245, 115, 245, 95, width=10, fill='white')