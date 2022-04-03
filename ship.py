from shutil import move
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
        self.velocity = 1
        self.MAX_VEL = 10

        # load bmp image and get rectangle
        self.image = pg.image.load('images/icons8-space-shuttle-100.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put spaceship on the bottom of window
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left

    def create(self):
        self.screen.blit(self.image, self.rect)
    
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            if self.rect.top + self.velocity > self.screen_rect.top + 10:
                self.increaseVelocity()
                self.rect.top -= self.velocity
        elif keys[pg.K_DOWN]:
            if self.rect.bottom - self.velocity < self.screen_rect.bottom - 10:
                self.increaseVelocity()
                self.rect.bottom += self.velocity
        else:
            self.velocity = 1

    def increaseVelocity(self):
        if self.velocity <= self.MAX_VEL:
            self.velocity += 1
