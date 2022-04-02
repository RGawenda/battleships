import sys
import pygame
from pygame import KEYDOWN, K_ESCAPE, QUIT
from pygame_menu.examples.other.maze import BLUE, RED

class Generate_board:
    def __init__(self, screen):
        k = 50
        while k < 501:
            l = 50
            while l < 501:
                pygame.draw.rect(screen, BLUE, (k, l, 50, 50))
                l = l + 50
            k = k + 50

class Game_board:
    def __init__(self):
        matrix: list[list[int]] = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    def get_value(self, x, y):
        return self.a[x][y]

    def set_value(self, x, y, z):
        self.a[x][y] = z

class Game:
    def __init__(self, screen):
        screen.fill((0, 0, 0))
        Generate_board(screen)
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

