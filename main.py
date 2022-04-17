import pygame as pg
from game import Game
from game import Level
from settings import Settings
from button import Button 
from button import State

class Main():

    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Settings().screen_width, Settings().screen_height))
        self.background = pg.Surface((Settings().screen_width, Settings().screen_height))
        self.bg_level_image = pg.image.load(Settings().button_image)
        self.bg_level_rect = self.bg_level_image.get_rect()
        pg.display.set_caption("The Quest")
        self.font = pg.font.Font(None, 30) 
        self.run_level_selection()

    def run_level_selection(self):
        self.level_one_button = Button(self.background)
        self.level_two_button = Button(self.background)
        self.level_three_button = Button(self.background)
        self.level_four_button = Button(self.background)
        self.level_one_button.set_state(State.selected)

        while True:
            self.check_events()
            self.screen.blit(self.background, (0, 0))
            self.background.blit(self.bg_level_image, self.bg_level_rect)
            self.level_text = self.font.render("THE QUEST", True, (255, 255, 255))
            self.screen.blit(self.level_text, (10, 10)) 
            
            self.level_one_button.draw_button(400, 100, 150, 100)
            self.level_text_1 = self.font.render("Instructions", True, (0, 0, 0))
            self.screen.blit(self.level_text_1, (415, 135)) 
            
            self.level_two_button.draw_button(400, 250, 150, 100)
            self.level_text_2 = self.font.render("Level 1", True, (0, 0, 0))
            self.screen.blit(self.level_text_2, (440, 290)) 
            
            self.level_three_button.draw_button(400, 400, 150, 100)
            self.level_text_3 = self.font.render("Level 2", True, (0, 0, 0))
            self.screen.blit(self.level_text_3, (440, 440)) 
            
            self.level_four_button.draw_button(400, 550, 150, 100)
            self.level_text_4 = self.font.render("Level 3", True, (0, 0, 0))
            self.screen.blit(self.level_text_4, (440, 590))
            pg.display.flip()

    def run_game(self, level):
        clock = pg.time.Clock()
        game = Game(self.screen, level)
        
        while True:
            clock.tick(Settings().FPS)
            self.check_events()
            game.update_screen()
            game.game_control()

    def show_instructions():
        print("To do")
    
    # Handling user's events    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or ( 
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_TAB:
                if self.level_one_button.get_state() == State.selected:
                    print("Boton 1")
                    self.level_two_button.set_state(State.selected)
                    self.level_one_button.set_state(State.unselected)
                elif self.level_two_button.get_state() == State.selected:
                    print("Boton 2")
                    self.level_three_button.set_state(State.selected)
                    self.level_two_button.set_state(State.unselected)
                elif self.level_three_button.get_state() == State.selected:
                    print("Boton 3")
                    self.level_four_button.set_state(State.selected)
                    self.level_three_button.set_state(State.unselected)
                elif self.level_four_button.get_state() == State.selected:
                    print("Boton 4")
                    self.level_one_button.set_state(State.selected)
                    self.level_four_button.set_state(State.unselected)
        
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                if self.level_one_button.get_state() == State.selected:
                    print("Boton 1")
                    self.show_instructions()
                elif self.level_two_button.get_state() == State.selected:
                    print("Boton 2")
                    self.run_game(Level.One)
                elif self.level_three_button.get_state() == State.selected:
                    print("Boton 3")
                    self.run_game(Level.Two)
                elif self.level_four_button.get_state() == State.selected:
                    print("Boton 4")
                    self.run_game(Level.Three)

Main()