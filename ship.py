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
        self.rotated = False

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

    def rotate_ship(self, angle):
        width = self.rect.x + self.screen_rect.width - self.rect.width
        if self.rotation_step == Rotation_Step.Nothing:
            angle = angle / 4
            width = self.rect.x + (self.screen_rect.width / 4) - self.rect.width
            self.rotation_step = Rotation_Step.One
        
        elif self.rotation_step == Rotation_Step.One:
            angle = angle / 2
            width = self.rect.x + (self.screen_rect.width / 2) - self.rect.width
            self.rotation_step = Rotation_Step.Two

        elif self.rotation_step == Rotation_Step.Two:
            angle = angle * 3 / 4 
            width = self.rect.x + (self.screen_rect.width * 3 / 4) - self.rect.width
            self.rotation_step = Rotation_Step.Three

        elif self.rotation_step == Rotation_Step.Three:
            self.rotation_step = Rotation_Step.Final 

        pos = (width, self.rect.y)
        w = self.rect.x
        h = self.rect.y
        originPos = (w, h)

        box = [pg.math.Vector2(p) for p in [(0, 0), (w, 0), (w, -h), (0, -h)]]
        box_rotate = [p.rotate(angle) for p in box]
        min_box = (min(box_rotate, key=lambda p: p[0])[0], min(box_rotate, key=lambda p: p[1])[1])
        max_box = (max(box_rotate, key=lambda p: p[0])[0], max(box_rotate, key=lambda p: p[1])[1])

        # calculate the translation of the pivot
        pivot = pg.math.Vector2(originPos[0], -originPos[1])
        pivot_rotate = pivot.rotate(angle)
        pivot_move = pivot_rotate - pivot

        # calculate the upper left origin of the rotated image
        origin = (pos[0] - originPos[0] + min_box[0] - pivot_move[0], pos[1] - originPos[1] - max_box[1] + pivot_move[1])

        # get a rotated image
        rotated_image = pg.transform.rotate(self.image, angle)

        # rotate and blit the image
        self.screen.blit(rotated_image, origin)
