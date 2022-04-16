import sys

import pygame
from pygame import QUIT

from ships import Carrier
from show_grid import Generate_board
from show_ships import Show_ships, Show_ship


class Show_grid:
    pass


class Set_ships:
    def __init__(self, screen, grid_of_game, image):
        setting = True


        carr = Carrier(700, 100, True)
        while setting:
            screen.blit(image, (0, 0))
            Show_ships(screen)
            Generate_board(screen, grid_of_game, True, False)
            Show_ship(screen, carr)

            for event in pygame.event.get():

                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_position = pygame.mouse.get_pos()
                        x, y = mouse_position
                        if carr.x < x < carr.x + 50 and carr.y < y < carr.y + 50:
                            carr.set_x(x)
                            print(carr.get_x())
                            carr.set_y(y)

            pygame.display.update()
        pass
