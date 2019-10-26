"""
    Programa escrito por: Nicole Rodriguez
"""
from Tkinter import *

class Nicole:
    def funcion(self, figura):
        vs = Toplevel()
        vs.configure(bg="gray")
        vs.title(figura)
        panel = Canvas(vs, width=600, height=500, bg="gray")
        panel.pack()
        # contorno
        panel.create_polygon(92, 30, 148, 30, 174, 84, 148, 110, 200, 110, 229, 140, 255, 113,
                             255, 193, 229, 220, 92, 220, 65, 194, 65, 140, 90, 112, 66, 86, 66, 58, width=1,
                             fill="#FFC914")
        # Alita
        panel.create_line(120, 140, 120, 166, width=4, fill="#ff9f04")
        panel.create_line(120, 166, 146, 194, width=4, fill="#ff9f04")
        panel.create_line(146, 194, 201, 193, width=4, fill="#ff9f04")
        panel.create_line(201, 193, 227, 166, width=4, fill="#ff9f04")
        panel.create_line(227, 166, 202, 140, width=4, fill="#ff9f04")
        panel.create_line(202, 140, 172, 140, width=4, fill="#ff9f04")
        # Ojito
        panel.create_oval(94, 72, 106, 86, width=4, fill="black")
        # Piquito
        panel.create_polygon(66, 86, 90, 112, 40, 112, width=4, fill="#ff9f04")
        # Agua
        panel.create_rectangle(0, 220, 600, 440, width=0, fill="#22d8cf")
        # Arena
        panel.create_rectangle(0, 438, 600, 520, width=0, fill="#fffa70")
        # conchita
        panel.create_polygon(249, 420, 285, 420, 302, 438, 304, 458, 266, 475, 254, 476, 248, 472, width=2,
                             fill="#ff88c3")
        panel.create_polygon(266, 475, 254, 476, 266, 482, width=2, fill="#ff88c3")
        panel.create_polygon(254, 476, 248, 460, 242, 466, width=2, fill="#ff88c3")
        # cuerpo pescadito
        panel.create_polygon(31, 290, 42, 302, 60, 308, 74, 318, 88, 333, 88, 348, 73, 348, 45, 333, 43, 330,
                             37, 319, 31, 305, width=2, fill="#2682b4")
        # aletas pescadito
        panel.create_polygon(60, 308, 60, 290, 74, 305, 74, 318, width=2, fill="#f98ea9")
        panel.create_polygon(59, 333, 45, 348, 45, 333, width=2, fill="#f98ea9")
        panel.create_polygon(37, 319, 29, 319, 15, 305, 31, 305, width=2, fill="#f98ea9")
        # cola pescadito
        panel.create_polygon(31, 290, 30, 275, 45, 260, 44, 275, 59, 275, width=2, fill="#f98ea9")