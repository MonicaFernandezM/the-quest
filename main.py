import pygame as pg
from game import Game
from settings import Settings
from button import Button 

class Main():

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Settings().screen_width, Settings().screen_height))
        #self.screen.fill((6, 36, 117))
        self.background = pg.Surface((Settings().screen_width, Settings().screen_height))
        self.background.fill((6, 36, 117))
        pg.display.set_caption("The Quest")
        self.font = pg.font.Font(None, 30) 
        self.run_level_selection()
        #self.run_game()

    def run_level_selection(self):
        self.level_one_button = Button(self.background)
        self.level_two_button = Button(self.background)

        while True:
            self.check_events()
            self.screen.blit(self.background, (0, 0))
            self.level_text = self.font.render("Mensaje de bienvenida", True, (255, 255, 255))
            self.screen.blit(self.level_text, (10, 10)) 
            self.level_one_button.draw_button(10, 10, 50, 30)
            self.level_two_button.set_selected()
            self.level_two_button.draw_button(10, 60, 50, 30)
            pg.display.flip()

    def run_game(self):
        clock = pg.time.Clock()
        game = Game(self.screen)
        
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