import sys

import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE
from pygame_menu.examples.other.maze import RED


class Show_winner:
    def __init__(self, screen, win):
        font = pygame.font.SysFont(None, 30)
        screen.fill((0, 0, 0))
        running = True
        while running:
            if win == 1:
                screen.blit(font.render('You Won', True, RED), (550, 300))
            else:
                screen.blit(font.render('Defeat', True, RED), (550, 300))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()
