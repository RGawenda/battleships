import pygame


class Ship_collision:
    def __init__(self, ships):
        self.number_of_ship = 0
        self.selected = False
        mouse_position = pygame.mouse.get_pos()
        x, y = mouse_position

        for a in range(0, len(ships)):
            if ships[a].direction:
                if ships[a].x < x < ships[a].x + ships[a].get_long() * 50 + ships[a].get_long():
                    if ships[a].y < y < ships[a].y + 50:
                        self.number_of_ship = a
                        self.selected = True
            else:
                if ships[a].y < y < ships[a].y + ships[a].get_long() * 50 + ships[a].get_long():
                    if ships[a].x < x < ships[a].x + 50:
                        self.number_of_ship = a
                        self.selected = True
