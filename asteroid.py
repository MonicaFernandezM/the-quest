import pygame as pg
import random 
from settings import Settings 

class Asteroid():

    def __init__(self, screen):
        self.screen = screen
        self.settings = Settings()
        self.velocity = random.randint(self.settings.max_asteroid_velocity, self.settings.min_asteorid_velocity)
    
        self.value = random.randint(1, len(self.settings.asteroid_images))
        self.image = pg.image.load(self.settings.asteroid_point.get(self.value))

        len_random = random.randint(self.settings.min_image_size, self.settings.max_image_size)
        self.image = pg.transform.scale(self.image, (len_random, len_random))
        self.rect = self.image.get_rect()

        self.screen_rect = screen.get_rect()
        top_random = random.randint(self.settings.bar_height, self.screen_rect.height - len_random)
        self.rect.top = top_random
        self.rect.right = self.screen_rect.right

    def create(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        if self.rect.right + self.velocity > self.screen_rect.left:
            self.rect.right -= self.velocity
        else:
            self.rect.right = self.screen_rect.right

    def reached_end(self) -> bool:
        if self.rect.right < self.screen_rect.left:
            return True
        return False 

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

