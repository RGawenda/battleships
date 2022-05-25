import pygame
from pygame_menu.examples.other.maze import BLACK, BLUE, RED, GREY


class Generate_board:
    def __init__(self, screen, board, player, pos2):
        font = pygame.font.SysFont(None, 40)
        pos = 0
        if pos2:
            pos = 600

        for k in range(0, 10):
            for l in range(0, 10):
                o = board.get_object(k, l).get_status()
                screen.blit(font.render(chr(65 + l), True, BLACK), (115 + (l * 50) + l + pos, 70))
                if k < 9:
                    screen.blit(font.render(chr(49 + k), True, BLACK), (70 + pos, 115 + (k * 50) + k))
                else:
                    screen.blit(font.render('10', True, BLACK), (60 + pos, 115 + (k * 50) + k))

                if player:
                    if o == 0:
                        color = BLUE
                    elif o == 1:
                        color = GREY
                    elif o == 3:
                        color = RED
                    elif o == 2:
                        color = BLACK
                else:
                    if o == 0 or o == 1:
                        color = BLUE
                    elif o == 3:
                        color = RED
                    elif o == 2:
                        color = BLACK

                Draw_grid((board.get_object(k, l).get_x() + pos), (board.get_object(k, l).get_y()), screen, color)


class Draw_grid:
    def __init__(self, x, y, screen, color):
        self.rect = None
        self.x = x
        self.y = y
        self.color = color
        pygame.draw.rect(screen, self.color, (x, y, 50, 50))
