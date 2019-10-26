# coding=utf-8
"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""
from Tkinter import *

class VictorHugo:
    """
    ElRichMC en Tkinter
    """

    # Metodo inicial
    def __init__(self):
        pass

    # Inicia la ventana hija con la figura de Steve
    def ventana_hija(self, figura):
        ventanahija = Toplevel()
        ventanahija.configure(bg='white')
        ventanahija.title(figura)

        ventanahija.iconbitmap('rich.ico')
        panel = Canvas(ventanahija, width=250, height=500, bg='white')
        panel.pack()
        #                                               ELRICHMC
        #                                           Brazo izquierdo
        panel.create_polygon(6, 126, 22, 122, 82, 124, 82, 324, 14, 330, 6, 318, width=1, fill="#0a0a08")  # Brazo base
        #
        #                                           Brazo derecho
        panel.create_polygon(186, 146, 232, 146, 232, 312, 188, 314, width=1, fill="#0a0a08")  # Brazo base
        #
        #                                             Piernas
        panel.create_polygon(62, 442, 77, 415, 98, 414, 98, 369, 115, 368, 115, 310,
                             165, 309, 165, 362, 180, 360, 187, 401, 185, 441,
                             88, 457, width=1, fill="#898989")
        #
        #                                               Pies
        panel.create_polygon(63, 470, 63, 442, 88, 457, 185, 441, 185, 468, 88, 485, width=1, fill="#282828")
        #
        #                                              Camisa
        panel.create_polygon(126, 179, 138, 179, 138, 295, 165, 295, 165, 310,
                             114, 310, 114, 297, 125, 297, width=1, fill="#181917")  # Parte negra
        panel.create_polygon(125, 165, 151, 165, 151, 310, 138, 310, 138, 180,
                             125, 180, width=1, fill="#861400")  # Parte roja
        #
        #                                           Cuerpo/capa
        panel.create_polygon(58, 449, 58, 326, 81, 324, 81, 132, 186, 134, 235, 142, 234, 312,
                             190, 315, 190, 402, 175, 362, 164, 362, 165, 296, 150, 296,
                             151, 166, 126, 165, 126, 298, 114, 298, 116, 368, 100, 369,
                             100, 414, 86, 417, 80, 414, width=1, fill="#0a0b08")
        #
        #                                           Cara de ElRichMC
        panel.create_polygon(102, 10, 202, 22, 202, 137, 104, 132, width=1, fill="#333333")  # Cara frontal
        panel.create_polygon(52, 32, 102, 10, 104, 132, 52, 133, width=1, fill="#1c1c1c")  # Parte trasera
        panel.create_polygon(116, 72, 142, 72, 142, 88, 116, 86, width=1, fill="#060606")  # Ojo izquierdo
        panel.create_polygon(168, 76, 190, 78, 192, 92, 166, 90, width=1, fill="#060606")  # Ojo derecho
        panel.create_polygon(128, 104, 180, 106, 180, 121, 128, 118, width=1, fill="#060606")  # Boca (sho te amo)
        #
        #                                           Decoración
        panel.create_polygon(6, 126, 22, 122, 82, 124, 82, 138, 24, 136, 6, 140, width=1, fill="#530800")  # Decoración - capa roja
        panel.create_polygon(5, 142, 6, 157, 9, 157, 11, 156, 11, 141, 18, 139, 18, 155, 21, 155,
                             23, 154, 23, 138, 31, 137, 31, 153, 37, 153, 38, 154, 46, 154,
                             46, 138, 62, 138, 63, 153, 64, 155, 78, 155, 78, 139, 84, 139,
                             84, 155, 113, 156, 113, 173, 126, 173, 126, 143, 100, 143,
                             99, 135, 88, 135, 88, 140, width=1,
                             fill="#d3ac00")  # Decoración - capa roja / decoración
        panel.create_polygon(186, 146, 232, 146, 234, 132, 214, 132, 214, 142, 186, 140, width=1,
                             fill="#530800")  # Decoración - capa roja
        panel.create_polygon(235, 148, 235, 161, 224, 161, 224, 147, 211, 146, 211, 160, 199, 160,
                             199, 146, 195, 147, 193, 159, 168, 159, 167, 174, 154, 175,
                             154, 181, 151, 180, 151, 153, 155, 152, 155, 145, 175, 146,
                             176, 139, 185, 140, 186, 146, 195, 147, width=1,
                             fill="#d3ac00")  # Decoración - capa roja / decoración