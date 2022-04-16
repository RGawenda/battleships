import sys
import pygame
from pygame import QUIT
from pygame_menu.examples.other.maze import BLUE
import game


class Select_mode:
    def __init__(self, screen):
        self.screen = screen
        self.mode = 0
        self.screen = pygame.display.set_mode((400, 300))

        running = True

        while running:
            mouse = pygame.mouse.get_pos()
            x, y = mouse
            pygame.draw.rect(screen, BLUE, (50, 50, 300, 50))
            pygame.draw.rect(screen, BLUE, (50, 101, 300, 50))
            pygame.draw.rect(screen, BLUE, (50, 152, 300, 50))
            pygame.draw.rect(screen, BLUE, (50, 203, 300, 50))

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if 50 < x < 350 and 50 < y < 100:
                            self.mode = 1
                            running = False
                            pass
                        elif 50 < x < 350 and 101 < y < 151:
                            self.mode = 2
                            running = False
                            pass
                        elif 50 < x < 350 and 152 < y < 202:
                            self.mode = 3
                            running = False
                            pass
                        elif 50 < x < 350 and 203 < y < 253:
                            running = False
                            pass
            pygame.display.update()
        pass


class Multiplayer_mode:
    def __init__(self, screen):
        self.mode = Select_mode(screen)
        if self.mode.mode > 0:
            game.Game(screen, self.mode)
        pass
