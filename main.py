import game
import pygame
import pygame_menu
import option

class Main_menu:
    def start_the_singleplayer_game(self):
        game.Game(self.screen)
        pass

    def start_the_multiplayer_game(self):
        game.Game(self.screen)
        pass

    def option(self):
        option.menu_option(self.screen)
        pass

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((400, 300))
        self.menu = pygame_menu.Menu('Batlleships', 400, 300, theme=pygame_menu.themes.THEME_DARK)
        self.menu.add.button('Singleplayer', self.start_the_singleplayer_game)
        self.menu.add.button('Multiplayer', self.start_the_multiplayer_game)
        self.menu.add.button('Option', self.option)
        self.menu.add.button('Exit', pygame_menu.events.EXIT)

        k = self.menu.mainloop(self.screen)
        pass

if __name__ == "__main__":
    Main_menu()
