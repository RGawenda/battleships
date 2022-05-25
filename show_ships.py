import pygame
from pygame_menu.examples.other.maze import BLACK, RED, WHITE


class Show_ship:
    def __init__(self, screen, ship, selected):
        self.ship = ship
        x1 = 0
        y1 = 0
        for a in range(0, self.ship.get_long()):
            if ship.direction:
                x1 = (a * 50) + a
            else:
                y1 = (a * 50) + a
            if selected:
                pygame.draw.rect(screen, WHITE, (self.ship.x + x1 - 3, self.ship.y + y1 - 3, 56, 56))
            pygame.draw.rect(screen, RED, (self.ship.x + x1, self.ship.y + y1, 50, 50))

class Show_set_ships_text:
    def __init__(self, screen):
        font = pygame.font.SysFont(None, 30)
        screen.blit(font.render('Ship placement', True, BLACK), (550, 20))

        pygame.draw.rect(screen, RED, (1075, 590, 100, 50))
        screen.blit(font.render('Save', True, BLACK), (1100, 600))
        pygame.draw.rect(screen, RED, (875, 590, 100, 50))
        screen.blit(font.render('Random', True, BLACK), (885, 600))

class Show_ships:
    def __init__(self, screen, ships, selected_ship, selected):
        for a in range(0, len(ships)):
            if selected:
                if a == selected_ship:
                    Show_ship(screen, ships[a], True)
                else:
                    Show_ship(screen, ships[a], False)
            else:
                Show_ship(screen, ships[a], False)

