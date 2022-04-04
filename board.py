import pygame
from pygame_menu.examples.other.maze import BLUE, RED, BLACK

class Generate_board:
    def __init__(self, screen, board):
        k = 0
        while k < 10:
            l = 0
            while l < 10:
                o = board.get_value(k, l)
                if(o == 0 or o == 1):
                    Grid((l*50)+100+l, (k*50)+100+k, screen, BLUE)
                elif(o == 3):
                    Grid((l*50)+100+l, (k*50)+100+k, screen, RED)
                elif (o == 2):
                    Grid((l * 50) + 100 + l, (k * 50) + 100 + k, screen, BLACK)
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

class Game_board:
    def __init__(self):
        self.matrix = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        pass

    def get_value(self, x, y):
        return self.matrix[x][y]
        pass

    def increment_value(self, x, y):
        self.matrix[x][y] = self.matrix[x][y] + 2
        pass

class Test_click:
    def __init__(self, board, pos):
        x, y = pos
        k = 0
        while k < 10:
            l = 0
            while l < 10:
                x1 = (l * 50) + 100 + l
                y1 = (k * 50) + 100 + k
                if ( x1 < x and x < x1+50 and y1 < y and y < y1+50):
                    if (board.get_value(k, l) < 2):
                        board.increment_value(k, l)
                l = l + 1
            k = k + 1
        pass
