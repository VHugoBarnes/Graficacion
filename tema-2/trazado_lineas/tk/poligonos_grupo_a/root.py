# coding=utf-8
"""
    Programa escrito por: Víctor Hugo Vázquez Gómez
"""
from Tkinter import *
import alfredo, brandon, cassandra, cynthiaLizeth, david, eduardoLeal, erickAlexis, franciscoJavier, jesus, kenneth, luis, nicole, victorHugo

class GrupoA:
    """
    Las figuras del grupo A graficación 2019
    Alumnos:

    1. Alfredo Santos
    2. Brandon Esquivel
    3. Cassandra González
    4. Cynthia Lizeth Barron Morales
    5. David Martinez
    6. Eduardo Leal
    7. Erick Alexis Gallegos Ruiz
    8. Francisco Javier Muñoz Rios
    9. Jesus De La Cruz
    10. Kenneth Mtz
    11. Luis Molina
    12. Nicole Rodríguez González
    13. Víctor Hugo Vázquez Gómez
    """

    def __init__(self):
        pass


    def ventana_hija(self, num):

        if num == 1:  # Alfredo Santos
            var1 = alfredo.Alfredo()
            var1.mostrar('Programa por Alfredo Santos')
        elif num == 2:  # Brandon Esquivel
            var2 = brandon.Brandon()
            var2.funcion('Programa por Brandon Esquivel')
        elif num == 3:  # Cassandra González
            var3 = cassandra.Cassandra()
            var3.mostrar('Programa por Cassandra Gónzalez')
        elif num == 4:  # Cynthia Lizeth
            var4 = cynthiaLizeth.CynthiaLizeth()
            var4.funcion('Programa por Cynthia Lizeth Barron Morales')
        elif num == 5:  # David Martinez
            var5 = david.David()
            var5.mostrar('Programa por David Martinez')
        elif num == 6:  # Eduardo Leal
            var6 = eduardoLeal.EduardoLeal()
            var6.poligono('Programa por Eduardo Leal')
        elif num == 7:  # Erick Alexis Gallegos Ruiz
            var7 =  erickAlexis.ErickAlexis()
            var7.mostrar('Programa por Erick Alexis Gallegos Ruiz')
        elif num == 8:  # Francisco Javier Muñoz Rios
            var8 = franciscoJavier.FranciscoJavier()
            var8.funcion('Programa por Francisco Javier Muñoz Rios')
        elif num == 9:  # Jesus De La Cruz
            var9 = jesus.Jesus()
            var9.mostrar('Programa por Jesus De La Cruz')
        elif num == 10:  # Kenneth Mtz
            var10 = kenneth.Kenneth()
            var10.funcion('Programa por Kenneth Mtz')
        elif num == 11:  # Luis Molina
            var11 = luis.Luis()
            var11.funcion('Programa por Luis Molina')
        elif num == 12:  # Nicole Rodríguez González
            var12 = nicole.Nicole()
            var12.funcion('Programa por Nicole Rodríguez González')
        elif num == 13:  # Víctor Hugo Vázquez Gómez
            var13 = victorHugo.VictorHugo()
            var13.ventana_hija('Programa por Víctor Hugo Vázquez Gómez')


    def ventana_padre(self):
        ventana_raiz = Tk()
        ventana_raiz.geometry("520x225")
        ventana_raiz.configure(bg='#d3abf5')
        ventana_raiz.title('Figuras')
        ventana_raiz.iconbitmap('Favicon.ico')

        color_boton = "#9C7FB5"
        color_letra = "#2E2536"

        # Menú
        boton1 = Button(ventana_raiz, text='Alfredo Santos - Bambi', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(1),)
        boton2 = Button(ventana_raiz, text='Brandon Esquivel - DJ Marshmello', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(2))
        boton3 = Button(ventana_raiz, text='Cassandra Gónzalez - Perrito', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(3))
        boton4 = Button(ventana_raiz, text='Cynthia Barron Morales - Mickey Mouse', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(4))
        boton5 = Button(ventana_raiz, text='David Martinez - Lobo', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(5))
        boton6 = Button(ventana_raiz, text='Eduardo Leal - Mega Man', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(6))
        boton7 = Button(ventana_raiz, text='Erick Alexis Gallegos - Astronauta', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(7))
        boton8 = Button(ventana_raiz, text='Francisco Javier Muñoz - Ganso', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(8))
        boton9 = Button(ventana_raiz, text='Jesus De La Cruz - Naruto', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(9))
        boton10 = Button(ventana_raiz, text='Kenneth Mtz - Arcade', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(10))
        boton11 = Button(ventana_raiz, text='Luis Molina - Gatito', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(11))
        boton12 = Button(ventana_raiz, text='Nicole Rodríguez González - Patito', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(12))
        boton13 = Button(ventana_raiz, text='Víctor Hugo Vázquez - ElRichMC/Minecraft', bg=color_boton, fg=color_letra,
                        command=lambda: self.ventana_hija(13))

        boton1.grid(column=1, row=1, ipadx=49, pady=3, padx=3)
        boton2.grid(column=1, row=2, ipadx=19, pady=3, padx=3)
        boton3.grid(column=1, row=3, ipadx=33, pady=3, padx=3)
        boton4.grid(column=1, row=4, ipadx=2, pady=3, padx=3)
        boton5.grid(column=1, row=5, ipadx=50, pady=3, padx=3)
        boton6.grid(column=1, row=6, ipadx=40, pady=3, padx=3)
        boton7.grid(column=1, row=7, ipadx=20, pady=3, padx=3)

        boton8.grid(column=3, row=1, ipadx=47, pady=3, padx=3)
        boton9.grid(column=3, row=2, ipadx=62, pady=3, padx=3)
        boton10.grid(column=3, row=3, ipadx=72, pady=3, padx=3)
        boton11.grid(column=3, row=4, ipadx=77, pady=3, padx=3)
        boton12.grid(column=3, row=5, ipadx=38, pady=3, padx=3)
        boton13.grid(column=3, row=6, ipadx=15, pady=3, padx=3)

        ventana_raiz.mainloop()