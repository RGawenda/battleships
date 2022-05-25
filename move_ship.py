import random

import pygame


class Change_ship_position:
    def __init__(self, ship):
        mouse_position = pygame.mouse.get_pos()
        x, y = mouse_position

        ship.set_x(x - 25)
        ship.set_y(y - 25)


class Change_ship_orientation:
    def check_grid_long(self, ship, k, l):
        if ship.direction:
            if l + ship.get_long() > 10:
                return False
        else:
            if k + ship.get_long() > 10:
                return False
        return True

    def check_ship_colision(self, ships, number, ship_on_the_grid, grid):
        for b in range(1, ships[number].get_long()):
            if ships[number].direction:
                if grid.get_object(ship_on_the_grid[number][1], ship_on_the_grid[number][2] + b).get_status() == 1:
                    return False
            else:
                if grid.get_object(ship_on_the_grid[number][1] + b, ship_on_the_grid[number][2]).get_status() == 1:
                    return False
        return True

    def __init__(self, ships, ship_on_the_grid, number_of_ship, grid):
        ship = ships[number_of_ship]

        if ship_on_the_grid[number_of_ship][0]:
            k = ship_on_the_grid[number_of_ship][1]
            l = ship_on_the_grid[number_of_ship][2]
            if self.check_grid_long(ship, k, l) and self.check_ship_colision(ships, number_of_ship, ship_on_the_grid,
                                                                             grid):
                if ship.direction:
                    for a in range(0, ship.get_long()):
                        grid.get_object(k + a, l).remove_ship()
                    ship.direction = False
                else:
                    for a in range(0, ship.get_long()):
                        grid.get_object(k, l + a).remove_ship()
                    ship.direction = True
        else:
            if ship.direction:
                ship.direction = False
            else:
                ship.direction = True


def save(ships):
    mouse_position = pygame.mouse.get_pos()
    x, y = mouse_position
    if 1075 < x < 1175 and 590 < y < 640:
        for ship in ships:
            if not ship[0]:
                return False
        return True


def random_ships(ships, grid_o, ships_on_grid, grid, if_bot):
    mouse_position = pygame.mouse.get_pos()
    x, y = mouse_position
    if 875 < x < 975 and 590 < y < 640 or if_bot:
        for i in range(0, 10):
            for j in range(0, 10):
                grid.get_object(i, j).remove_ship()
        for a in range(0, len(ships)):
            ll = False
            while not ll:
                direction = random.randrange(0, 2)

                if direction:
                    xx = random.randrange(0, 11 - ships[a].get_long())
                    yy = random.randrange(0, 10)
                else:
                    xx = random.randrange(0, 10)
                    yy = random.randrange(0, 11 - ships[a].get_long())

                ships[a].set_direction(direction)
                ships[a].set_x(grid.get_object(xx, yy).get_x())
                ships[a].set_y(grid.get_object(xx, yy).get_y())

                grid_o.set_ship_of_grid(ships[a], ships_on_grid, a)
                ll = grid_o.get_t()
