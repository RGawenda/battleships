import pygame
from pygame_menu.examples.other.maze import BLACK, RED


class Show_ship:
    def __init__(self, screen, ship):
        self.ship = ship
        x1 = 0
        y1 = 0
        for a in range(0, self.ship.get_long()):
            if ship.direction:
                x1 = (a * 50) + a
            else:
                y1 = (a * 50) + a
            pygame.draw.rect(screen, RED, (self.ship.x + x1, self.ship.y + y1, 50, 50))

        pass

class Show_set_ships_text:
    def __init__(self, screen):
        font = pygame.font.SysFont(None, 30)
        screen.blit(font.render('Setting ships', True, BLACK), (550, 20))
        pass

class Show_ships:
    def __init__(self, screen, ships):
        for a in range(0, len(ships)):
            Show_ship(screen, ships[a])
        pass

