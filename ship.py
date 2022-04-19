import pygame as pg 
import sys
from settings import Settings 
from enum import Enum

class Rotation_Step(Enum):
    Nothing = 0
    One = 1
    Two = 2
    Three = 3
    Final = 4

class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.rotation_step = Rotation_Step.Nothing
        self.settings = Settings()
        # load bmp image and get rectangle
        self.image = pg.image.load(self.settings.ship_image)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put spaceship on the bottom of window
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        self.is_rotated = False

    def create(self):
        self.screen.blit(self.image, self.rect)
    
    def move(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_UP]:
            self.move_up()
        elif keys[pg.K_DOWN]:
            self.move_down()
        else:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                    mouse = pg.mouse.get_pressed()
                    if mouse[0]:
                        position = pg.mouse.get_pos()
                        mouse_y = position[1]
                        if mouse_y < self.rect.top:
                            self.move_up()
                        elif mouse_y > self.rect.bottom:
                            self.move_down()
                    else:
                        self.settings.ship_velocity = 1        
                
    def move_up(self):
        if self.rect.top + self.settings.ship_velocity > self.screen_rect.top + 10:
            self.increaseVelocity()
            self.rect.top -= self.settings.ship_velocity

    def move_down(self):        
        if self.rect.bottom - self.settings.ship_velocity < self.screen_rect.bottom - 10:
            self.increaseVelocity()
            self.rect.bottom += self.settings.ship_velocity

    def increaseVelocity(self):
        if self.settings.ship_velocity <= self.settings.max_ship_velocity:
            self.settings.ship_velocity += 1

    def rotate_ship(self, angle, rect):
        if self.is_rotated != True:
            self.image = pg.transform.rotate(self.image, angle)
            self.is_rotated = True

    def move_rotated_ship(self, velocity):
        if self.rect.right + velocity < self.screen_rect.right:
            self.rect.right += velocity
