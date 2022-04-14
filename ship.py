import pygame as pg 
import sys
from settings import Settings 

class Ship():
    def __init__(self, screen):
        self.screen = screen
    
        # load bmp image and get rectangle
        self.image = pg.image.load(Settings().ship_image)
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
            if self.rect.top + Settings.ship_velocity > self.screen_rect.top + 10:
                self.increaseVelocity()
                self.rect.top -= Settings.ship_velocity
        elif keys[pg.K_DOWN]:
            if self.rect.bottom - Settings.ship_velocity < self.screen_rect.bottom - 10:
                self.increaseVelocity()
                self.rect.bottom += Settings.ship_velocity
        else:
            Settings.ship_velocity = 1

    def increaseVelocity(self):
        if Settings.ship_velocity <= Settings().max_ship_velocity:
            Settings.ship_velocity += 1
