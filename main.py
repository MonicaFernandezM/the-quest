import pygame as pg
from game import Game, Level, Result
from settings import Settings
from welcome import Welcome, Selection

class Main():

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Settings().screen_width, Settings().screen_height))
        pg.display.set_caption("The Quest")

        self.run_welcome()

    def run_welcome(self):
        self.welcome = Welcome(self, self.screen)
        
        while True:
            self.welcome.check_events()
            self.welcome.update_screen()
        
    def run_game(self, level):
        clock = pg.time.Clock()
        self.game = Game(self.screen, level)
        
        while True:
            clock.tick(Settings().FPS)
            self.check_events()
            self.game.update_screen()
            self.game.game_control()
            print("result ", self.game.game_result)
            if self.game.game_result == Result.Win:
                if level == Selection.Level_one:
                    self.game.switch_level(Level.Two)
                elif level == Selection.Level_two:
                    self.game.switch_level(Level.Three)
    
    # Handling user's events    
    def check_events(self):
        
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()

Main()