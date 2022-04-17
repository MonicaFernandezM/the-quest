import pygame as pg
from enum import Enum
from settings import Settings

class State(Enum):
    unselected = 1
    selected = 2
    pressed = 3

class Button():
    def __init__(self, surface):

        self.state = State.unselected
        self.surface = surface

    def set_selected(self):
        self.state = State.selected

    def draw_button(self, left, top, width, height):
        if self.state == State.unselected:
            self.color = (255, 0, 255)
        elif self.state == State.selected:
            self.color = (255, 255, 0)
        
        self.button_rect = pg.draw.rect(self.surface, (0, 255, 255), pg.Rect(left, top, width, height))
        self.line_one = pg.draw.line(self.surface, self.color, (left, top), (left, height + top), 6)
        self.line_two = pg.draw.line(self.surface, self.color, (left, top), (width + left, top), 6)
        self.line_tree = pg.draw.line(self.surface, self.color, (left, height + top), (width + left, top + height), 6)
        self.line_four = pg.draw.line(self.surface, self.color, (width + left, top), (width + left, top + height), 6)