

class Get_grid:
    def __init__(self, grid_game):
        self.grid = grid_game
        self.x2 = 0
        self.y2 = 0
        self.t = False

    def remove_ship_from_grid(self, ship):
        for k in range(0, 10):
            for l in range(0, 10):
                x1 = self.grid.get_object(k, l).get_x()
                y1 = self.grid.get_object(k, l).get_y()
                if x1 < ship.x + 25 < x1 + 50 and y1 < ship.y + 25 < y1 + 50:
                    if ship.direction:
                        if k + ship.get_long() < 11:
                            for a in range(0, ship.get_long()):
                                self.grid.get_object(k + a, l).remove_ship()
                    else:
                        if l + ship.get_long() < 11:
                            for a in range(0, ship.get_long()):
                                self.grid.get_object(k, l + a).remove_ship()

    def check_grid(self, ship):
        self.t = False
        self.x2 = 0
        self.y2 = 0
        for k in range(0, 10):
            for l in range(0, 10):
                x1 = self.grid.get_object(k, l).get_x()
                y1 = self.grid.get_object(k, l).get_y()
                if x1 < ship.x + 25 < x1 + 50 and y1 < ship.y + 25 < y1 + 50:
                    self.x2 = k
                    self.y2 = l
                    if self.grid.get_object(k, l).get_status() == 0:
                        for a in range(0, ship.get_long()):
                            if ship.direction:
                                if k + ship.get_long() < 11:
                                    self.t = True
                                    if self.grid.get_object(k + a, l).get_status() != 0:
                                        self.t = False
                                        break
                            else:
                                if l + ship.get_long() < 11:
                                    self.t = True
                                    if self.grid.get_object(k, l + a).get_status() != 0:
                                        self.t = False
                                        break

    def get_t(self):
        return self.t

    def set_ship_of_grid(self, ship, ship_on_the_grid, number):

        self.check_grid(ship)

        if self.t:
            ship.x = self.grid.get_object(self.x2, self.y2).get_x()
            ship.y = self.grid.get_object(self.x2, self.y2).get_y()
            for a in range(0, ship.get_long()):
                if ship.direction:
                    self.grid.get_object(self.x2 + a, self.y2).set_ship()
                else:
                    self.grid.get_object(self.x2, self.y2 + a).set_ship()
            ship_on_the_grid[number][0] = True

            ship_on_the_grid[number][1] = self.x2
            ship_on_the_grid[number][2] = self.y2
