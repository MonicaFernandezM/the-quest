import pygame as pg
from game import Game
from game import Level
from settings import Settings
from welcome import Welcome, Selection
from records import Records, Record

class Main():

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Settings().screen_width, Settings().screen_height))
        pg.display.set_caption("The Quest")

        self.records = Records()
        #record1 = Record("Monica", 200)
        #self.records.add_record(record1)

        record2 = Record("Sabrina", 100)
        self.records.add_record(record2)

        #self.run_welcome()

    def run_welcome(self):
        self.welcome = Welcome(self.screen)
        
        while True:
            self.check_events()
            self.welcome.update_screen()
        
    def run_game(self, level):
        clock = pg.time.Clock()
        self.game = Game(self.screen, level)
        
        while True:
            clock.tick(Settings().FPS)
            self.check_events()
            self.game.update_screen()
            self.game.game_control()
    
    # Handling user's events    
    def check_events(self):
        
        for event in pg.event.get():
            if event.type == pg.QUIT or ( 
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
            elif event.type == pg.KEYDOWN and (event.key == pg.K_TAB or event.key == pg.K_DOWN):
                self.welcome.change_states()
        
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                selection = self.welcome.option_selected()
                self.call_game(selection)

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pressed()
                if mouse[0]:
                    position = pg.mouse.get_pos()
                    mouse_x = position[0]
                    mouse_y = position[1]
                    selection = self.welcome.handle_mouse_event(mouse_x, mouse_y)
                    self.call_game(selection)
        
    def call_game(self, selection):
        if selection == Selection.Level_one:
            self.run_game(Level.One)
        elif selection == Selection.Level_two:
            self.run_game(Level.Two)
        elif selection == Selection.Level_three:
            self.run_game(Level.Three)

    def next_level(self):
        

Main()