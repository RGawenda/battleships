import pygame
import pygame_menu

import game


class MainMenu:
    def start_the_singleplayer_game(self):
        game.Game(self.screen, False, False)

    def start_the_multiplayer_game(self):
        game.Game(self.screen, True, False)

    def load_save(self):
        game.Game(self.screen, True, True)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.menu = pygame_menu.Menu('Battleships', 400, 300, theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.button('Singleplayer', self.start_the_singleplayer_game)
        self.menu.add.button('Multiplayer', self.start_the_multiplayer_game)
        self.menu.add.button('Save', self.load_save)
        self.menu.add.button('Exit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)


if __name__ == "__main__":
    MainMenu()
