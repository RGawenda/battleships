import pygame
from pygame_menu.examples.other.maze import BLUE, RED, BLACK

class Generate_board:
    def __init__(self, screen, board):
        font = pygame.font.SysFont(None, 40)

        for k in range(0, 10):
            for l in range(0, 10):
                o = board.get_object(k, l).get_status()
                screen.blit(font.render(chr(65+l), True, BLACK), (115+(l*50)+l, 70))
                if(k < 9):
                    screen.blit(font.render(chr(49 + k), True, BLACK), (70, 115 + (k * 50) + k))
                else:
                    screen.blit(font.render('10', True, BLACK), (60, 115 + (k * 50) + k))

                if(o == 0 or o == 1):
                    Draw_grid((board.get_object(k, l).get_x()), (board.get_object(k, l).get_y()), screen, BLUE)
                elif(o == 3):
                    Draw_grid((board.get_object(k, l).get_x()), (board.get_object(k, l).get_y()), screen, RED)
                elif (o == 2):
                    Draw_grid((board.get_object(k, l).get_x()), (board.get_object(k, l).get_y()), screen, BLACK)
        pass

class Draw_grid:
    def __init__(self, x, y, screen, color):
        self.rect = None
        self.x = x
        self.y = y
        self.color_ = color
        pygame.draw.rect(screen, self.color_, (x, y, 50, 50))
        pass

class Grid_element:
    def __init__(self, x, y):
        self.status = 0
        self.x = x
        self.y = y
        pass

    def get_status(self):
        return self.status
        pass

    def get_x(self):
        return self.x
        pass

    def get_y(self):
        return self.y
        pass

    def change_status(self):
        self.status = self.status + 2
        pass

class Game_board:
    def __init__(self):
        matrix = []
        for i in range(0, 10):
            row = []
            for j in range(0, 10):
                x1 = (j * 50) + 100 + j
                y1 = (i * 50) + 100 + i
                row.append(Grid_element(x1, y1))
            matrix.append(row)
        self.matrix = matrix
        pass

    def get_object(self, x, y):
        return self.matrix[x][y]
        pass

class Test_click:
    def __init__(self, board, pos):
        x, y = pos
        for k in range(0, 10):
            for l in range(0, 10):
                x1 = board.get_object(k, l).get_x()
                y1 = board.get_object(k, l).get_y()
                if ( x1 < x and x < x1+50 and y1 < y and y < y1+50):
                    if (board.get_object(k, l).get_status() < 2):
                        board.get_object(k, l).change_status()
        pass
