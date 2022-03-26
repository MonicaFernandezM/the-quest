import pygame as pg

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
    