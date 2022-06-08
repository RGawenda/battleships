import random

from tkinter import filedialog

import pygame
from pygame_menu.examples.other.maze import BLACK, RED

import save
from grid import GridStructure


class GameSelector:
    def __init__(self):
        self.handler = None
        self.turn = True
        self.win1 = 0
        self.win2 = 0
        self.pos1 = 0, 0
        self.num = 0

    def bot(self, grid: GridStructure):
        while not self.turn:
            if self.num == 0:
                x = random.randrange(0, 10)
                y = random.randrange(0, 10)
                if grid.get_object(x, y).get_status() < 2:
                    if grid.get_object(x, y).get_status() == 1:
                        self.win2 += 1
                        self.pos1 = x, y
                        self.num += 1
                    grid.get_object(x, y).change_status()
                    self.turn = True
            else:
                x, y = self.pos1
                a = 0
                b = 0
                if self.num == 1:
                    if x + 1 < 10:
                        a = 1
                        b = 0
                elif self.num == 2:
                    if y + 1 < 10:
                        a = 0
                        b = 1
                elif self.num == 3:
                    if x - 1 > -1:
                        a = -1
                        b = 0
                elif self.num == 4:
                    if y - 1 > -1:
                        a = 0
                        b = -1
                if a != 0 or b != 0:
                    if grid.get_object(x + a, y + b).get_status() < 2:
                        if grid.get_object(x + a, y + b).get_status() == 1:
                            self.win2 += 1
                        grid.get_object(x + a, y + b).change_status()
                        self.turn = True
                    else:
                        if self.num != 4:
                            self.num += 1
                        else:
                            self.num = 0
                else:
                    if self.num != 4:
                        self.num += 1
                    else:
                        self.num = 0

    def player(self, grid: GridStructure, pos_click, player):
        if self.turn == player:
            pos_grid = 0
            if not player:
                pos_grid = 600
            x, y = pos_click
            for i in range(0, 10):
                for j in range(0, 10):
                    grid_x = grid.get_object(i, j).get_x()
                    grid_y = grid.get_object(i, j).get_y()
                    if grid_x + pos_grid < x < grid_x + 50 + pos_grid and grid_y < y < grid_y + 50:
                        if grid.get_object(i, j).get_status() < 2:
                            if grid.get_object(i, j).get_status() == 1:
                                if not player:
                                    self.win2 += 1
                                else:
                                    self.win1 += 1
                            grid.get_object(i, j).change_status()
                            if player:
                                self.turn = False
                            else:
                                self.turn = True

    def create_handler(self, path):
        handler = None
        if ".txt" in path:
            handler = save.TextFileHandler()
        else:
            handler = save.JsonFileHandler()
        return handler

    def check_winner(self):
        if self.win1 == 17:
            return 1
        elif self.win2 == 17:
            return 2
        else:
            return 0

    def get_turn(self):
        return self.turn

    def set_turn(self, turn):
        self.turn = turn

    def run_save(self, grid_of_game, enemy_grid, mode):
        mouse_position = pygame.mouse.get_pos()
        x, y = mouse_position
        if 1075 < x < 1175 and 670 < y < 720:
            path = filedialog.asksaveasfilename(defaultextension='.txt')
            self.handler = self.create_handler(path)
            self.handler.save(grid_of_game, enemy_grid, self.turn, mode, path)


class ShowTextInGame:
    def __init__(self, mode):
        self.mode = mode
        self.font = pygame.font.SysFont(None, 30)

    def show_text(self, screen):
        pygame.draw.rect(screen, RED, (1075, 670, 100, 50))
        screen.blit(self.font.render('Save', True, BLACK), (1100, 680))
        if self.mode:
            a = 'player 2 map'
            b = 'player 1 map'
        else:
            a = 'bot map'
            b = 'player map'
        screen.blit(self.font.render(a, True, BLACK), (450, 20))
        screen.blit(self.font.render(b, True, BLACK), (750, 20))

    def show_turn(self, screen, player_turn):
        if self.mode:
            if player_turn:
                c = 'turn: player 1'
            else:
                c = 'turn: player 2'
        else:
            if player_turn:
                c = 'turn: player'
            else:
                c = 'turn: computer'
        screen.blit(self.font.render(c, True, BLACK), (50, 20))
