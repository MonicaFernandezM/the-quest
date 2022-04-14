import pygame as pg
from game import Game
from settings import Settings

class Main():

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Settings().screen_width, Settings().screen_height))
        self.screen.fill((6, 36, 117))
        pg.display.set_caption("The Quest")
        #self.run_level_selection()
        self.run_game()

    def run_level_selection(self):
        while True:
            self.check_events()
            self.font = pg.font.Font(None, 30)
            self.level_text = self.font.render("Mensaje de bienvenida", True, (255, 255, 255)) 
            self.screen.blit(self.level_text, (10, 10)) 
            pg.display.flip()

    def run_game(self):
        clock = pg.time.Clock()
        game = Game(self.screen)
        game.setup_screen()
        
        while True:
            clock.tick(Settings().FPS)
            self.check_events()
            game.update_screen()
            game.game_control()
    
    # Handling user's events    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or ( 
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()

Main()