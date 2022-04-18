import pygame

class Change_ships_position:
    def __init__(self, ships, xt, yt):
        for a in range(0, len(ships)):
            Change_ship_position(ships[a], xt, yt)
        pass

class Change_ship_position:
    def __init__(self, ship, xt, yt):
        if ship.x < xt < ship.x + 50 and ship.y < yt < ship.y + 50:
            mouse_position = pygame.mouse.get_pos()
            x, y = mouse_position

            ship.set_x(x - 25)
            ship.set_y(y - 25)
        pass


class Change_ship_orientation:
    def __init__(self, ship):
        mouse_position = pygame.mouse.get_pos()
        x, y = mouse_position
        if ship.x < x < ship.x + 50 and ship.y < y < ship.y + 50:
            if ship.direction:
                ship.direction = False
            else:
                ship.direction = True
        pass

class Change_ships_orientation:
    def __init__(self, ships):
        for a in range(0, len(ships)):
            Change_ship_orientation(ships[a])
        pass
