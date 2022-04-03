import sys
import pygame
import Board
from pygame import KEYDOWN, K_ESCAPE, QUIT



class Game:
    def __init__(self, screen):
        screen.fill((0, 0, 0))

        board = Board.Game_board()

        running = True

        while running:
            Board.Generate_board(screen, board)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button ==1:
                        mouse_position = pygame.mouse.get_pos()
                        Board.Test_click(board, mouse_position)

            pygame.display.update()
        pass
