import sys
import pygame
import board
from pygame import KEYDOWN, K_ESCAPE, QUIT



class Game:
    def __init__(self, screen):
        screen = pygame.display.set_mode((1280, 720))
        screen.fill((0, 0, 0))
        map = board.Game_board()
        pygame.display.set_caption('Image')
        image = pygame.image.load(r'background.png')
        image = pygame.transform.scale(image, (1280, 720))
        screen.blit(image, (0, 0))
        running = True

        while running:

            board.Generate_board(screen, map)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        screen = pygame.display.set_mode((400, 300))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button ==1:
                        mouse_position = pygame.mouse.get_pos()
                        board.Test_click(map, mouse_position)

            pygame.display.update()
        pass
