import pygame as pg

class Asteroid():
    def __init__(self, screen):
        self.screen = screen

        # load bmp image and get rectangle
        self.image = pg.image.load('images/icons8-planet-100.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #put asteroid on the right side of window
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

    def create(self):
        self.screen.blit(self.image, self.rect)

