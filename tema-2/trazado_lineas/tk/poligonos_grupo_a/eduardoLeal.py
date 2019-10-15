from Tkinter import *

class EduardoLeal:
    def poligono(self, titulo):
        v1 = Toplevel()
        v1.title(titulo)
        v1.protocol("wn_DELETE_WINDOW", "onexit")
        v1.geometry("600x600")

        panel = Canvas(v1, width=1000, height=600, bg="cyan")
        panel.pack()
        # cuerpo
        panel.create_polygon(96, 110, 137, 110, 290, 110, 317, 137, 289, 164, 275, 179, 275, 317, 220, 303, 221, 276,
                             206, 261, 165, 275, 151, 276, 109, 247, 109, 234, 123, 220, 165, 220, 165, 179, 96, 165,
                             width=1, fill="#6BE0FF", outline="black")
        # mano
        panel.create_polygon(289, 109, 303, 82, 325, 60, 337, 62, 344, 82, 344, 55, 330, 55, 330, 42, 345, 27, 372, 28,
                             385, 41, 385, 69, 317, 137, width=1, fill="#2063FF", outline="black")
        # buster
        panel.create_polygon(96, 165, 96, 178, 54, 178, 41, 164, 13, 165, 14, 151, 0, 137, 13, 124, 13, 110, 41, 109,
                             55, 96, 96, 96, 96, 109, width=1, fill="#2063FF", outline="black")
        # pies
        panel.create_polygon(165, 275, 152, 316, 137, 331, 82, 331, 68, 317, 68, 303, 96, 276, 109, 234, 123, 220,
                             width=1, fill="#2063FF", outline="black")
        panel.create_polygon(275, 303, 275, 330, 261, 344, 261, 399, 246, 413, 220, 412, 206, 399, 206, 330, 220, 316,
                             220, 289, width=1, fill="#2063FF", outline="black")
        # cabeza
        panel.create_polygon(138, 137, 138, 68, 275, 68, 275, 137, 234, 179, 179, 178, width=1, fill="#FFF595",
                             outline="black")
        # cara
        panel.create_polygon(151, 137, 179, 137, 179, 82, 138, 82, 138, 110, width=1, fill="#FFFFFF", outline="black")
        panel.create_polygon(165, 124, 179, 124, 179, 96, 165, 96, width=1, fill="#000000", outline="black")

        panel.create_polygon(193, 137, 193, 82, 234, 82, 248, 96, 248, 124, 234, 138, width=1, fill="#FFFFFF",
                             outline="black")
        panel.create_polygon(193, 124, 220, 124, 220, 96, 193, 96, width=1, fill="#000000", outline="black")

        panel.create_polygon(179, 137, 207, 138, 220, 151, 220, 164, 207, 179, 179, 178, 165, 165, 165, 151, width=1,
                             fill="#000000", outline="black")
        # armor
        panel.create_polygon(247, 137, 247, 165, 275, 137, 275, 55, 249, 28, 220, 28, 193, 55, 193, 69, 165, 69, 165,
                             55, 151, 55, 137, 69, 137, 82, 165, 82, 165, 96, 193, 96, 193, 83, 234, 82, 261, 108, 261,
                             137, width=1, fill="#2063FF", outline="black")
        panel.create_polygon(275, 220, 275, 248, 235, 261, 207, 261, 165, 220, width=1, fill="#2063FF", outline="black")
        # accesorios
        panel.create_polygon(0, 137, 13, 124, 82, 124, 70, 137, width=1, fill="#6BE0FF", outline="black")
        panel.create_polygon(165, 68, 165, 55, 193, 27, 220, 27, 193, 55, 193, 68, width=1, fill="#6BE0FF",
                             outline="black")