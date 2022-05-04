from cmath import rect
import pygame as pg
from settings import Settings
from button import Button 
from button import State
from enum import Enum

class Selection(Enum):
    Instruction = 0
    Level_one = 1
    Level_two = 2
    Level_three = 3

class Welcome():
    def __init__(self, screen):
        self.screen = screen
        self.bg_level_image = pg.image.load(Settings().button_image)
        self.bg_level_rect = self.bg_level_image.get_rect()
        self.font = pg.font.Font(None, 30)
        self.inst_font = pg.font.Font(None, 25)
        self.show_inst = False

        self.level_one_button = Button(self.screen)
        self.level_two_button = Button(self.screen)
        self.level_three_button = Button(self.screen)
        self.level_four_button = Button(self.screen)
        self.level_one_button.set_state(State.selected)
        self.close_button = Button(self.screen)

    def update_screen(self):
        self.screen.blit(self.bg_level_image, self.bg_level_rect)

        self.level_text = self.font.render("THE QUEST", True, (255, 255, 255))
        self.screen.blit(self.level_text, (420, 30)) 
        
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

        if self.show_inst:
            screen_rect = self.screen.get_rect()
            rect = screen_rect
            rect.x += 20
            rect.y += 20
            rect.width -= 40
            rect.height -= 40

            rect.centerx = screen_rect.centerx
            rect.centery = screen_rect.centery
            pg.draw.rect(self.screen, (56, 94, 209), rect)

            self.inst_text_0 = self.font.render("Instrucciones", True, (0, 0, 0))
            self.screen.blit(self.inst_text_0, (40, 50))

            self.inst_text_1 = self.inst_font.render("Para seleccionar el nivel, usa la tecla TAB  de tu teclado para seleccionarlo y ENTER para elegirlo.", True, (0, 0, 0))
            self.screen.blit(self.inst_text_1, (40, 100))

            self.inst_text_2 = self.inst_font.render("Para jugar usa las teclas ARRIBA y ABAJO de tu teclado.", True, (0, 0, 0))
            self.screen.blit(self.inst_text_2, (40, 140))

            self.inst_text_3 = self.inst_font.render("También puedes hacer click con el botón IZQUIERDO de tu ratón.", True, (0, 0, 0))
            self.screen.blit(self.inst_text_3, (40, 180))

            self.inst_text_4 = self.inst_font.render("Cada asteroide esquivado te dará puntos. Intenta llegar al final para conquistar la luna.", True, (0, 0, 0))
            self.screen.blit(self.inst_text_4, (40, 220))

            self.close_button.draw_button(400, 550, 150, 100)
            self.close_text = self.font.render("Close", True, (0, 0, 0))
            self.screen.blit(self.close_text, (445, 590))

        pg.display.flip()

    def show_instructions(self):
        self.show_inst = True
    
    def hide_instructions(self):
        self.show_inst = False

    def change_states(self):
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
        
    def handle_mouse_event(self, mouse_x, mouse_y) -> Selection:
        if mouse_x > self.level_one_button.button_rect.left and \
            mouse_x < self.level_one_button.button_rect.right:
            # x location is the same for all buttons
            if mouse_y > self.level_one_button.button_rect.top and \
                mouse_y < self.level_one_button.button_rect.bottom:
                self.show_instructions()
            elif mouse_y > self.level_two_button.button_rect.top and \
                mouse_y < self.level_two_button.button_rect.bottom:
                #self.run_game(Level.One)
                return Selection.Level_one
            elif mouse_y > self.level_three_button.button_rect.top and \
                mouse_y < self.level_three_button.button_rect.bottom:
                #self.run_game(Level.Two)
                return Selection.Level_two
            elif mouse_y > self.level_four_button.button_rect.top and \
                mouse_y < self.level_four_button.button_rect.bottom and \
                self.show_inst == False:
                #self.run_game(Level.Three)
                return Selection.Level_three

            elif mouse_y > self.close_button.button_rect.top and \
                mouse_y < self.close_button.button_rect.bottom and \
                self.show_inst == True:
                self.hide_instructions()

        return Selection.Instruction

    def option_selected(self) -> Selection:
        if self.level_one_button.get_state() == State.selected:
            self.show_instructions()
            return Selection.Instruction
        elif self.level_two_button.get_state() == State.selected:
            #self.run_game(Level.One)
            return Selection.Level_one
        elif self.level_three_button.get_state() == State.selected:
            #self.run_game(Level.Two)
            return Selection.Level_two
        elif self.level_four_button.get_state() == State.selected:
            #self.run_game(Level.Three)
            return Selection.Level_three