# -*- coding: utf-8 -*-

import pygame
import webcolors
import itertools

pygame.init()

window = pygame.display.set_mode((250, 500))

colors = itertools.cycle(['green', 'blue', 'purple', 'pink', 'red', 'orange'])

clock = pygame.time.Clock()

color_base = next(colors)
color_siguiente = next(colors)
color_actual = color_base

FPS = 60
segundos = 3.
pasos = segundos * FPS
paso = 1

corriendo = True

while corriendo:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            corriendo = False
            pygame.quit()
            exit()

    paso += 1
    if paso < pasos:
        # (y-x)/pasos  Calcula la cantidad de cambios por paso que se requieren
        # para desvanecer el color antiguo al color nuevo.
        # Lo multiplicamos con el contador de pasos actual
        color_actual = [x + (((y-x)/pasos)*paso) for x, y in zip(pygame.color.Color(color_base), pygame.color.Color(color_siguiente))]
    else:
        paso = 1
        color_base = color_siguiente
        color_siguiente = next(colors)

    pygame.draw.rect(window, color_actual, (0, 0, 250, 500), 0)
    #                                               ELRICHMC
    #                                           Brazo izquierdo
    color_brazo = webcolors.hex_to_rgb("#0a0a08")
    pygame.draw.polygon(window, color_brazo, [(6, 126), (22, 122), (82, 124), (82, 324), (14, 330), (6, 318)], 0)  # Brazo base
    #
    #                                           Brazo derecho
    pygame.draw.polygon(window, color_brazo, [(186, 146), (232, 146), (232, 312), (188, 314)], 0)  # Brazo base
    #
    #                                             Piernas
    color_pierna = webcolors.hex_to_rgb("#898989")
    pygame.draw.polygon(window, color_pierna, [(62, 442), (77, 415), (98, 414), (98, 369), (115, 368), (115, 310),
                                               (165, 309), (165, 362), (180, 360), (187, 401), (185, 441),
                                               (88, 457)], 0)
    #
    #                                               Pies
    color_pie = webcolors.hex_to_rgb("#282828")
    pygame.draw.polygon(window, color_pie, [(63, 470), (63, 442), (88, 457), (185, 441), (185, 468), (88, 485)], 0)
    #
    #                                              Camisa
    color_camisa_negro = webcolors.hex_to_rgb("#181917")
    color_camisa_rojo = webcolors.hex_to_rgb("#861400")
    pygame.draw.polygon(window, color_camisa_negro, [(126, 179), (138, 179), (138, 295), (165, 295), (165, 310),
                                                     (114, 310), (114, 297), (125, 297)], 0)  # Parte negra
    pygame.draw.polygon(window, color_camisa_rojo, [(125, 165), (151, 165), (151, 310), (138, 310), (138, 180),
                                                    (125, 180)], 0)  # Parte roja
    #
    #                                           Cuerpo/capa
    color_cuerpo = webcolors.hex_to_rgb("#0a0b08")
    pygame.draw.polygon(window, color_cuerpo, [(58, 449), (58, 326), (81, 324), (81, 132), (186, 134), (235, 142),
                                               (234, 312), (190, 315), (190, 402), (175, 362), (164, 362),
                                               (165, 296), (150, 296), (151, 166), (126, 165), (126, 298),
                                               (114, 298), (116, 368), (100, 369), (100, 414), (86, 417), (80, 414)], 0)
    #
    #                                           Cara de ElRichMC
    color_cara_frontal = webcolors.hex_to_rgb("#333333")
    color_cara_trasera = webcolors.hex_to_rgb("#1c1c1c")
    color_ojo_boca = webcolors.hex_to_rgb("#060606")
    pygame.draw.polygon(window, color_cara_frontal, [(102, 10), (202, 22), (202, 137), (104, 132)], 0)  # Cara frontal
    pygame.draw.polygon(window, color_cara_trasera, [(52, 32), (102, 10), (104, 132), (52, 133)], 0)  # Parte trasera
    pygame.draw.polygon(window, color_ojo_boca, [(116, 72), (142, 72), (142, 88), (116, 86)], 0)  # Ojo izquierdo
    pygame.draw.polygon(window, color_ojo_boca, [(168, 76), (190, 78), (192, 92), (166, 90)], 0)  # Ojo derecho
    pygame.draw.polygon(window, color_ojo_boca, [(128, 104), (180, 106), (180, 121), (128, 118)], 0)  # Boca
    #
    #                                           Decoración
    color_decoracion_rojo = webcolors.hex_to_rgb("#530800")
    color_decoracion_rojo_fuerte = webcolors.hex_to_rgb("#d3ac00")

    pygame.draw.polygon(window, color_decoracion_rojo, [(6, 126), (22, 122), (82, 124), (82, 138), (24, 136),
                                                        (6, 140)], 0)  # Decoración - capa roja
    pygame.draw.polygon(window, color_decoracion_rojo_fuerte, [(5, 142), (6, 157), (9, 157), (11, 156), (11, 141),
                                                               (18, 139), (18, 155), (21, 155), (23, 154), (23, 138),
                                                               (31, 137), (31, 153), (37, 153), (38, 154), (46, 154),
                                                               (46, 138), (62, 138), (63, 153), (64, 155), (78, 155),
                                                               (78, 139), (84, 139), (84, 155), (113, 156), (113, 173),
                                                               (126, 173), (126, 143), (100, 143), (99, 135), (88, 135),
                                                               (88, 140)], 0)  # Decoración - capa roja / decoración
    pygame.draw.polygon(window, color_decoracion_rojo, [(186, 146), (232, 146), (234, 132), (214, 132),
                                                        (214, 142), (186, 140)], 0)  # Decoración - capa roja
    pygame.draw.polygon(window, color_decoracion_rojo_fuerte, [(235, 148), (235, 161), (224, 161), (224, 147),
                                                               (211, 146), (211, 160), (199, 160), (199, 146),
                                                               (195, 147), (193, 159), (168, 159), (167, 174),
                                                               (154, 175), (154, 181), (151, 180), (151, 153),
                                                               (155, 152), (155, 145), (175, 146), (176, 139),
                                                               (185, 140), (186, 146), (195, 147)], 0)  # Decoración - capa roja / decoración
    pygame.display.update()
    clock.tick(FPS)
