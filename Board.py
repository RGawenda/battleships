import pygame
from pygame_menu.examples.other.maze import BLUE, RED


class Generate_board:
    def __init__(self, screen, board):
        k = 0
        while k < 10:
            l = 0
            while l < 10:
                if(board.get_value(k, l) == 0):
                    Grid((l*50)+100+l, (k*50)+100+k, screen, BLUE)
                else:
                    Grid((l*50)+100+l, (k*50)+100+k, screen, RED)
                l = l + 1
            k = k + 1
        pass

class Grid:
    def __init__(self, x, y, screen, color):
        self.rect = None
        self.x = x
        self.y = y
        self.color_ = color
        pygame.draw.rect(screen, self.color_, (x, y, 50, 50))

    def change(self):
        self.color_ = RED
        pass

    def click(self, event):
        x, y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(x, y):
                    self.change()
        pass

class Game_board:
    def __init__(self):
        self.matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        pass

    def get_value(self, x, y):
        return self.matrix[x][y]
        pass

    def set_value(self, x, y, z):
        self.matrix[x][y] = z
        pass
