import pygame




class Change_ship_position:
    def __init__(self, ship):
        mouse_position = pygame.mouse.get_pos()
        x, y = mouse_position

        ship.set_x(x - 25)
        ship.set_y(y - 25)
        pass


class Change_ship_orientation:
    def __init__(self, ship):
        if ship.direction:
            ship.direction = False
        else:
            ship.direction = True
        pass
