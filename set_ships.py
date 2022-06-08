import sys

import pygame
from pygame import QUIT, KEYDOWN, K_SPACE

import grid_operations
import move_ship
import ship_collision
from ships import Carrier, Battleship, Destroyer, Submarine, PatrolBoat
from show_grid import GenerateBoard
from show_ships import ShowShips, ShowSetShipsText


class SetShips:

    def create_ships(self):
        carr = Carrier(700, 100, True)
        bat = Battleship(700, 200, True)
        des = Destroyer(700, 300, True)
        sub = Submarine(700, 400, True)
        pat = PatrolBoat(700, 500, True)
        self.ships = [carr, bat, des, sub, pat]

    def __init__(self, screen, grid_of_game, image, if_bot):
        self.create_ships()
        setting = True
        t = False

        selected_ship = ship_collision.ShipCollision(self.ships)
        a = grid_operations.GetGrid(grid_of_game)
        get = False

        ship_on_the_grid = [[False, 0, 0], [False, 0, 0], [False, 0, 0], [False, 0, 0], [False, 0, 0]]
        if if_bot:
            move_ship.random_ships(self.ships, a, ship_on_the_grid, grid_of_game, if_bot)
            return
        while setting:
            screen.blit(image, (0, 0))
            ShowSetShipsText(screen)
            GenerateBoard(screen, grid_of_game, True, False)

            if not t:
                selected_ship = ship_collision.ShipCollision(self.ships)

            ShowShips(screen, self.ships, selected_ship.number_of_ship, selected_ship.selected)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        t = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        if move_ship.save(ship_on_the_grid):
                            setting = False
                        move_ship.random_ships(self.ships, a, ship_on_the_grid, grid_of_game, if_bot)
                        t = False
                if event.type == KEYDOWN:
                    if event.key == K_SPACE and selected_ship.selected:
                        move_ship.ChangeShipOrientation(self.ships, ship_on_the_grid, selected_ship.number_of_ship,
                                                          grid_of_game)
            if t and selected_ship.selected:
                if get and ship_on_the_grid[selected_ship.number_of_ship][0]:
                    get = False
                    a.remove_ship_from_grid(self.ships[selected_ship.number_of_ship])
                    ship_on_the_grid[selected_ship.number_of_ship][0] = False
                move_ship.ChangeShipPosition(self.ships[selected_ship.number_of_ship])
            else:
                a.set_ship_of_grid(self.ships[selected_ship.number_of_ship], ship_on_the_grid,
                                   selected_ship.number_of_ship)
                get = True
            pygame.display.update()
