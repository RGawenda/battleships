import sys
import pygame

import bot
import grid
from pygame import KEYDOWN, K_ESCAPE, QUIT

import set_ships
import show_grid
from win import Show_winner


class Game:
    def __init__(self, screen, game_mode):
        self.screen = screen
        self.game_mode = game_mode

        self.screen = pygame.display.set_mode((1280, 720))

        self.screen.fill((0, 0, 0))

        grid_of_game = grid.Grid_structure()
        enemy_grid = grid.Grid_structure()
        pygame.display.set_caption('Battleships')
        image = pygame.image.load(r'background.png')
        image = pygame.transform.scale(image, (1280, 720))
        self.screen.blit(image, (0, 0))

        set_ships.Set_ships(self.screen, grid_of_game, image, False)
        set_ships.Set_ships(self.screen, enemy_grid, image, True)
        self.screen.blit(image, (0, 0))
        gam = bot.Game_selector()
        running = True
        while running:
            gam.bot(grid_of_game)
            show_grid.Generate_board(screen, enemy_grid, False, False)
            show_grid.Generate_board(screen, grid_of_game, True, True)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        screen = pygame.display.set_mode((400, 300))
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_position = pygame.mouse.get_pos()
                        gam.player(enemy_grid, mouse_position)
            pygame.display.update()
            if gam.check_winner():
                running = False
        Show_winner(screen, gam.check_winner())
        self.screen = pygame.display.set_mode((400, 300))
