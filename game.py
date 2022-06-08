import sys
import pygame
from tkinter import filedialog

import save
import selector
import grid
from pygame import KEYDOWN, K_ESCAPE, QUIT

import set_ships
import show_grid
from win import ShowWinner


class Game:

    def create_handler(self, path):
        handler = None
        if ".txt" in path:
            handler = save.TextFileHandler()
        else:
            handler = save.JsonFileHandler()
        return handler

    def __init__(self, screen, multi, load_save):
        self.screen = screen
        self.multi = multi

        grid_of_game = grid.GridStructure()
        enemy_grid = grid.GridStructure()

        pygame.display.set_caption('Battleships')
        image = pygame.image.load(r'background.png')
        image = pygame.transform.scale(image, (1280, 720))
        gam = selector.GameSelector()

        if not load_save:
            self.screen = pygame.display.set_mode((1280, 720))
            set_ships.SetShips(self.screen, grid_of_game, image, False)
            set_ships.SetShips(self.screen, enemy_grid, image, not self.multi)
        else:
            path = filedialog.askopenfilename(filetypes=[('Zapisy gry (".txt", ".json")', ["*.txt", "*.json"])])
            self.handler = self.create_handler(path)
            data = self.handler.load(path)
            grid_of_game.import_grid(data["player grid"])
            enemy_grid.import_grid(data["enemy grid"])
            gam.set_turn(data["turn"])
            self.multi = data["mode"]

        self.screen = pygame.display.set_mode((1280, 720))
        self.screen.blit(image, (0, 0))
        turn = selector.ShowTextInGame(self.multi)


        running = True
        while running:
            if not self.multi:
                gam.bot(grid_of_game)
            self.screen.blit(image, (0, 0))

            show_grid.GenerateBoard(screen, enemy_grid, False, False)
            show_grid.GenerateBoard(screen, grid_of_game, not self.multi, True)

            turn.show_turn(screen, gam.get_turn())
            turn.show_text(screen)

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
                        gam.player(enemy_grid, mouse_position, True)
                        gam.run_save(grid_of_game, enemy_grid, self.multi)
                        if self.multi:
                            gam.player(grid_of_game, mouse_position, False)
            pygame.display.update()
            if gam.check_winner():
                running = False
        ShowWinner(screen, gam.check_winner(), self.multi)
        self.screen = pygame.display.set_mode((400, 300))

