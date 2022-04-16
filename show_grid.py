import pygame
from pygame_menu.examples.other.maze import BLACK, BLUE, RED


class Generate_board:
    def __init__(self, screen, board, player, pos2):
        font = pygame.font.SysFont(None, 40)
        pos = 0
        if pos2 == True:
            pos = 600

        for k in range(0, 10):
            for l in range(0, 10):
                o = board.get_object(k, l).get_status()
                if player:
                    o = o + 2
                screen.blit(font.render(chr(65 + l), True, BLACK), (115 + (l * 50) + l + pos, 70))
                if k < 9:
                    screen.blit(font.render(chr(49 + k), True, BLACK), (70 + pos, 115 + (k * 50) + k))
                else:
                    screen.blit(font.render('10', True, BLACK), (60 + pos, 115 + (k * 50) + k))

                if o == 0 or o == 1:
                    Draw_grid((board.get_object(k, l).get_x() + pos), (board.get_object(k, l).get_y()), screen, BLUE)
                elif o == 3:
                    Draw_grid((board.get_object(k, l).get_x() + pos), (board.get_object(k, l).get_y()), screen, RED)
                elif o == 2:
                    Draw_grid((board.get_object(k, l).get_x() + pos), (board.get_object(k, l).get_y()), screen, BLACK)
        pass


class Draw_grid:
    def __init__(self, x, y, screen, color):
        self.rect = None
        self.x = x
        self.y = y
        self.color = color
        pygame.draw.rect(screen, self.color, (x, y, 50, 50))
        pass
