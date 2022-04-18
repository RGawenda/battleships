import sys

import pygame
from pygame import QUIT, KEYDOWN, K_SPACE

import move_ship
from ships import Carrier, Battleship, Destroyer, Submarine, Patrol_Boat
from show_grid import Generate_board
from show_ships import Show_ships, Show_set_ships_text


class Show_grid:
    pass


class Set_ships:
    def __init__(self, screen, grid_of_game, image):
        setting = True
        t = False
        carr = Carrier(700, 100, True)
        bat = Battleship(700, 200, True)
        des = Destroyer(700, 300, True)
        sub = Submarine(700, 400, True)
        pat = Patrol_Boat(700, 500, True)
        ships = [carr, bat, des, sub, pat]

        while setting:
            screen.blit(image, (0, 0))
            Show_set_ships_text(screen)
            Generate_board(screen, grid_of_game, True, False)

            Show_ships(screen, ships)

            mouse_position = pygame.mouse.get_pos()
            x, y = mouse_position

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        t = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        t = False

                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        move_ship.Change_ships_orientation(ships)
            if t:
                move_ship.Change_ships_position(ships, x, y)

            pygame.display.update()
        pass
