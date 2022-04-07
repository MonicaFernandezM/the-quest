import pygame as pg
import random 

class Asteroid():

    images = ['images/icons8-astronauta-96.png', 
              'images/icons8-baby-yoda-96.png', 
              'images/icons8-ciencia-ficción-96.png', 
              'images/icons8-cometa-96.png', 
              'images/icons8-estrella-de-la-muerte-96.png', 
              'images/icons8-extraterrestre-96.png',
              'images/icons8-grey-96.png',
              'images/icons8-planeta-96.png',
              'images/icons8-satélites-96.png',
              'images/icons8-stormtrooper-96.png']

    def __init__(self, screen):
        self.screen = screen
        self.velocity = random.randint(2, 10)

        # load bmp image and get rectangle
        image_random = random.randint(1, len(self.images))
        self.image = pg.image.load(self.images[image_random - 1])
        len_random = random.randint(15, 80)
        self.image = pg.transform.scale(self.image, (len_random, len_random))
        self.rect = self.image.get_rect() # asteroid real size

        self.screen_rect = screen.get_rect()
        top_random = random.randint(0, self.screen_rect.height - len_random)
        self.rect.top = top_random
        self.rect.right = self.screen_rect.right

    def create(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        if self.rect.right + self.velocity > self.screen_rect.left:
            self.rect.right -= self.velocity
        else:
            self.rect.right = self.screen_rect.right

    def remove(self):
        self.rect.top = self.screen_rect.bottom
        self.rect.right = self.screen_rect.left

    def intersection(self, ship) -> bool:
        if self.rect.width > ship.rect.width:
            smaller_width = ship
            bigger_width = self
        else:
            smaller_width = self
            bigger_width = ship

        if self.rect.height > ship.rect.height:
            smaller_height = ship
            bigger_height = self
        else:
            smaller_height = self
            bigger_height = ship 

        left_collide = smaller_width.rect.x in range(bigger_width.rect.x, bigger_width.rect.x + bigger_width.rect.width)
        right_collide = smaller_width.rect.x + smaller_width.rect.width in range(bigger_width.rect.x, bigger_width.rect.x + bigger_width.rect.width)
        top_collide = smaller_height.rect.y in range(bigger_height.rect.y, bigger_height.rect.y + bigger_height.rect.height)
        bottom_collide = smaller_height.rect.y + smaller_height.rect.height in range(bigger_height.rect.y, bigger_height.rect.y + bigger_height.rect.height)
        
        return (left_collide or right_collide) and (top_collide or bottom_collide)
