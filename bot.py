import random

from grid import Grid_structure


class Game_selector:
    def __init__(self):
        self.turn = True
        self.win1 = 0
        self.win2 = 0
        self.pos1 = 0, 0
        self.num = 0

    def bot(self, grid: Grid_structure):
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
            elif self.num == 1:
                x, y = self.pos1
                if x + 1 < 10:
                    if grid.get_object(x+1, y).get_status() < 2:
                        if grid.get_object(x+1, y).get_status() == 1:
                            self.win2 += 1
                        grid.get_object(x+1, y).change_status()
                        self.turn = True
                    else:
                        self.num += 1
                else:
                    self.num += 1
            elif self.num == 2:
                x, y = self.pos1
                if y + 1 < 10:
                    if grid.get_object(x, y+1).get_status() < 2:
                        if grid.get_object(x, y+1).get_status() == 1:
                            self.win2 += 1
                        grid.get_object(x, y+1).change_status()
                        self.turn = True
                    else:
                        self.num += 1
                else:
                    self.num += 1
            elif self.num == 3:
                x, y = self.pos1
                if x - 1 > -1:
                    if grid.get_object(x-1, y).get_status() < 2:
                        if grid.get_object(x-1, y).get_status() == 1:
                            self.win2 += 1
                        grid.get_object(x-1, y).change_status()
                        self.turn = True
                    else:
                        self.num += 1
                else:
                    self.num += 1
            elif self.num == 4:
                x, y = self.pos1
                if y - 1 > -1:
                    if grid.get_object(x, y-1).get_status() < 2:
                        if grid.get_object(x, y-1).get_status() == 1:
                            self.win2 += 1
                        grid.get_object(x, y-1).change_status()
                        self.turn = True
                    else:
                        self.num = 0
                else:
                    self.num = 0


    def player(self, grid: Grid_structure, pos_click):
        if self.turn:
            x, y = pos_click
            for i in range(0, 10):
                for j in range(0, 10):
                    grid_x = grid.get_object(i, j).get_x()
                    grid_y = grid.get_object(i, j).get_y()
                    if grid_x < x < grid_x + 50 and grid_y < y < grid_y + 50:
                        if grid.get_object(i, j).get_status() < 2:
                            if grid.get_object(i, j).get_status() == 1:
                                self.win1 += 1
                            grid.get_object(i, j).change_status()
                            self.turn = False
        pass

    def check_winner(self):
        if self.win1 == 17:
            return 1
        elif self.win2 == 17:
            return 2
        else:
            return 0
