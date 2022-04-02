import sys
import pygame
from pygame import KEYDOWN, K_ESCAPE, QUIT

class Generate_board:
    def __init__(self):
        box = pygame.Rect(10,10,50,50)

class Game_board:
    def __init__(self):
        a: list[list[int]] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def get_value(self, x, y):
        return self.a[x][y]

    def set_value(self, x, y, z):
        self.a[x][y] = z

class Game:
    def __init__(self, screen):
        running = True
        while running:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
            pygame.display.update()

