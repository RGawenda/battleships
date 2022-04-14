import sys

import pygame
from pygame import QUIT
import show_grid




class Set_ships:
    def __init__(self, screen, map, image):

        setting = True
        screen.blit(image, (0, 0))
        while setting:

            show_grid.Generate_board(screen, map, 1)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button ==1:
                        mouse_position = pygame.mouse.get_pos()

            pygame.display.update()

        pass
