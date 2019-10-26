"""
programa escrito por: yolyrdz.blogspot.com
"""
from Tkinter import *
import pygame

pygame.init()

window = pygame.display.set_mode((1000,1000))
window.fill((255,255,255))
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        else:
            cara = (139, 130, 0)
            orejas = (139, 130, 85)
            menton = (255,78, 0)
            ojos = (0, 0, 0)
            nariz = (0, 0, 0)
            # cara
            pygame.draw.polygon(window, cara, [(415, 50), (235, 490), (365, 625), (755, 625), (850, 500), (700, 50)], 0)
            # orejas
            pygame.draw.polygon(window, orejas, [(415, 50), (60, 320), (175, 635)], 0)
            pygame.draw.polygon(window, orejas, [(700, 50), (1045, 320), (896, 635)], 0)
            # menton
            pygame.draw.polygon(window, menton, [(365, 625), (550, 415), (755, 625)],0)
            # ojos
            pygame.draw.ellipse(window, ojos, (420, 225, 80, 100))
            pygame.draw.ellipse(window, ojos, (630, 225, 80, 100))
            # bigotes
            pygame.draw.ellipse(window, ojos, (475, 525, 20, 20), 0)
            pygame.draw.ellipse(window, ojos, (615, 525, 20, 20), 0)
            pygame.draw.ellipse(window, ojos, (445, 560, 20, 20), 0)
            pygame.draw.ellipse(window, ojos, (610, 560, 20, 20), 0)
            pygame.draw.ellipse(window, ojos, (480, 560, 20, 20), 0)
            pygame.draw.ellipse(window, ojos, (640, 560, 20, 20), 0)
            # nariz
            pygame.draw.ellipse(window, nariz, (470, 305, 100, 140), 0)
            pygame.display.update()