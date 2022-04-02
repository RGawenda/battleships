import sys
from typing import List

import pygame
import pygame_menu


class game:



    pygame.init()
    screen = pygame.display.set_mode((1280,720))

    def set_difficulty(value, difficulty):
      # Do the job here !
     pass

    def start_the_singleplayer_game(self):
     # Do the job here !
     pass

    def start_the_multiplayer_game(self):
     # Do the job here !
     pass

    def option(self):
        # Do the job here !
        pass

    menu = pygame_menu.Menu('Welcome', 400, 300, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button('Singleplayer', start_the_singleplayer_game)
    menu.add.button('Multiplayer', start_the_multiplayer_game)
    menu.add.button('Option', option)
    menu.add.button('Exit', pygame_menu.events.EXIT)
    menu.mainloop(screen)

class game_board:
    a: list[list[int]] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def get_value(self, x, y):
        return self.a[x][y]

    def set_value(self, x, y, z):
        self.a[x][y] = z
