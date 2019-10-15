from Tkinter import *

class David:
    def mostrar(self, titulo):
        v1 = Toplevel()
        v1.title(titulo)
        v1.protocol("wn_DELETE_WINDOW", "onexit")
        v1.geometry("600x600")

        canvas1 = Canvas(v1, width=200, height=200, bg="black")
        canvas1.pack(expand=YES, fill=BOTH)
        canvas1.create_polygon(140, 20, 160, 20, 200, 40, 240, 80, 260, 100, 300, 80, 340, 100, 360, 80, 400, 40, 440,
                               20, 460, 20, 480, 80, 460, 140, 440, 200, 360, 140, 300, 200, 240, 140, 160, 200, 140,
                               140, 120, 80, width=5, fill=("#C6A58A"), outline="#FFFFFF")
        canvas1.create_polygon(160, 200, 240, 140, 300, 200, 360, 140, 440, 200, 460, 280, 480, 360, 460, 360, 440, 340,
                               380, 400, 320, 420, 280, 420, 220, 400, 160, 340, 140, 360, 120, 360, 140, 300, width=5,
                               fill=("#AF7A4E"), outline="#FFFFFF")
        canvas1.create_polygon(200, 220, 220, 220, 260, 240, 220, 240, width=5, fill=("yellow"), outline="#000000")
        canvas1.create_polygon(340, 240, 380, 220, 400, 220, 380, 240, width=5, fill=("yellow"), outline="#000000")
        canvas1.create_polygon(320, 220, 340, 300, width=5, fill=("black"), outline="#FFFFFF")
        canvas1.create_polygon(340, 300, 360, 340, width=5, fill=("black"), outline="#FFFFFF")
        canvas1.create_polygon(360, 340, 360, 360, width=5, fill=("black"), outline="#FFFFFF")
        canvas1.create_polygon(280, 220, 260, 300, width=5, fill=("black"), outline="#FFFFFF")
        canvas1.create_polygon(260, 300, 240, 340, width=5, fill=("black"), outline="#FFFFFF")
        canvas1.create_polygon(240, 340, 240, 360, width=5, fill=("black"), outline="#FFFFFF")
        canvas1.create_polygon(240, 360, 280, 380, width=5, fill=("black"), outline="#FFFFFF")
        canvas1.create_polygon(360, 360, 320, 380, width=5, fill=("black"), outline="#FFFFFF")
        canvas1.create_polygon(360, 360, 400, 280, width=5, fill=("black"), outline="#FFFFFF")
        canvas1.create_polygon(240, 360, 200, 280, width=5, fill=("black"), outline="#FFFFFF")
        canvas1.create_polygon(320, 380, 340, 340, 320, 320, 280, 320, 260, 340, 280, 380, width=5, fill=("black"),
                               outline="#FFFFFF")
        canvas1.create_polygon(220, 220, 240, 240, 220, 240, width=5, fill=("black"), outline="#000000")
        canvas1.create_polygon(380, 220, 380, 240, 360, 240, width=5, fill=("black"), outline="#000000")
        canvas1.create_polygon(160, 40, 160, 140, 180, 160, 220, 120, 220, 100, width=5, fill=("#AF7A4E"),
                               outline="#FFFFFF")
        canvas1.create_polygon(440, 40, 380, 100, 380, 120, 420, 160, 440, 140, width=5, fill=("#AF7A4E"),
                               outline="#FFFFFF")