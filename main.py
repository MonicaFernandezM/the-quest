from cmath import rect
import pygame as pg
from game import Game
from game import Level
from settings import Settings
from button import Button 
from button import State
from levels import Levels

class Main():
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((Settings().screen_width, Settings().screen_height))
        pg.display.set_caption("The Quest")
        self.show_inst = False 
        self.run_level_selection()

    def run_level_selection(self):
        self.run_levels()
        
    def run_game(self, level):
        clock = pg.time.Clock()
        game = Game(self.screen, level)
        
        while True:
            clock.tick(Settings().FPS)
            self.check_events()
            game.update_screen()
            game.game_control()

    def show_instructions(self):
        self.show_inst = True
    
    def hide_instructions(self):
        self.show_inst = False
    
    # Handling user's events    
    def check_events(self):
        
        for event in pg.event.get():
            if event.type == pg.QUIT or ( 
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
            elif event.type == pg.KEYDOWN and (event.key == pg.K_TAB or event.key == pg.K_DOWN):
                if self.level_one_button.get_state() == State.selected:
                    self.level_two_button.set_state(State.selected)
                    self.level_one_button.set_state(State.unselected)
                elif self.level_two_button.get_state() == State.selected:
                    self.level_three_button.set_state(State.selected)
                    self.level_two_button.set_state(State.unselected)
                elif self.level_three_button.get_state() == State.selected:
                    self.level_four_button.set_state(State.selected)
                    self.level_three_button.set_state(State.unselected)
                elif self.level_four_button.get_state() == State.selected:
                    self.level_one_button.set_state(State.selected)
                    self.level_four_button.set_state(State.unselected)

            #TODO: handle button exit
        
            elif event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
                if self.level_one_button.get_state() == State.selected:
                    self.show_instructions()
                elif self.level_two_button.get_state() == State.selected:
                    self.run_game(Level.One)
                elif self.level_three_button.get_state() == State.selected:
                    self.run_game(Level.Two)
                elif self.level_four_button.get_state() == State.selected:
                    self.run_game(Level.Three)

            if event.type == pg.MOUSEBUTTONDOWN:
                mouse = pg.mouse.get_pressed()
                if mouse[0]:
                    position = pg.mouse.get_pos()
                    mouse_x = position[0]
                    mouse_y = position[1]

                    if mouse_x > self.level_one_button.button_rect.left and \
                        mouse_x < self.level_one_button.button_rect.right:
                        # x location is the same for all buttons
                        if mouse_y > self.level_one_button.button_rect.top and \
                            mouse_y < self.level_one_button.button_rect.bottom:
                            self.show_instructions()
                        elif mouse_y > self.level_two_button.button_rect.top and \
                            mouse_y < self.level_two_button.button_rect.bottom:
                            self.run_game(Level.One)
                        elif mouse_y > self.level_three_button.button_rect.top and \
                            mouse_y < self.level_three_button.button_rect.bottom:
                            self.run_game(Level.Two)
                        elif mouse_y > self.level_four_button.button_rect.top and \
                            mouse_y < self.level_four_button.button_rect.bottom and \
                            self.show_inst == False:
                            self.run_game(Level.Three)
                        elif mouse_y > self.close_button.button_rect.top and \
                            mouse_y < self.close_button.button_rect.bottom and \
                            self.show_inst == True:
                           self.hide_instructions()
Main()