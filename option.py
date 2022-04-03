import sys

import pygame
from pygame import KEYDOWN, K_ESCAPE, QUIT


class menu_option:
    def __init__(self, screen):
        screen.fill((0, 0, 0))
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