import pygame
import pygame_menu

import game
import multiplayer
import option


class Main_menu:
    def start_the_singleplayer_game(self):
        game.Game(self.screen, 0)

    def start_the_multiplayer_game(self):
        self.mode = multiplayer.Select_mode(self.screen)
        if self.mode.mode > 0:
            game.Game(self.screen, self.mode)

    def option(self):
        option.Menu_option(self.screen)

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.menu = pygame_menu.Menu('Battleships', 400, 300, theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.button('Singleplayer', self.start_the_singleplayer_game)
        self.menu.add.button('Multiplayer', self.start_the_multiplayer_game)
        self.menu.add.button('Options', self.option)
        self.menu.add.button('Exit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)


if __name__ == "__main__":
    Main_menu()
