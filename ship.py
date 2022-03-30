import pygame as pg 
import sys
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Ship():
    def __init__(self, screen):
        self.screen = screen

        # load bmp image and get rectangle
        self.image = pg.image.load('images/icons8-space-shuttle-100.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put spaceship on the bottom of window
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

    def create(self):
        self.screen.blit(self.image, self.rect)
    
    def move(self, direction):
        if direction == Direction.UP:
            if self.rect.top + 5 > self.screen_rect.top:
                self.rect.top -=5
        elif direction == Direction.DOWN:
            if self.rect.bottom - 5 < self.screen_rect.bottom:
                self.rect.centery +=5

