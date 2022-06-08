import sys

import pygame
from pygame import QUIT, KEYDOWN, K_ESCAPE


class ShowWinner:

    def __init__(self, screen, win, mode):
        font = pygame.font.SysFont(None, 30)
        if mode:
            if win == 1:
                pygame.display.set_caption('win1')
                image = pygame.image.load(r'win1.png')
            else:
                pygame.display.set_caption('win2')
                image = pygame.image.load(r'win2.png')
        else:
            if win == 1:
                pygame.display.set_caption('WIN')
                image = pygame.image.load(r'win.png')
            else:
                pygame.display.set_caption('Defeat')
                image = pygame.image.load(r'defeat.png')

        image = pygame.transform.scale(image, (1280, 720))
        screen.blit(image, (0, 0))

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
