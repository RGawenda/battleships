import sys

import pygame
import pygame_menu
from pygame import KEYDOWN, K_ESCAPE, QUIT


class menu_option:
    def __init__(self, screen):
        screen.fill((0, 0, 0))

        self.screen = pygame.display.set_mode((1280, 720))
        self.menu_option = pygame_menu.Menu('Option', 400, 300, theme=pygame_menu.themes.THEME_DARK)
        self.menu_option.add.button('Back', )

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()
        pass