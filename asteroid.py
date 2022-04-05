import pygame as pg
import random 

class Asteroid():

    images = ['images/icons8-planet-100.png', 
              'images/icons8-baby-yoda-50.png', 
              'images/icons8-ciencia-ficción-50.png', 
              'images/icons8-estrella-de-la-muerte-50.png', 
              'images/icons8-extraterrestre-50.png', 
              'images/icons8-satélites-50.png']

    def __init__(self, screen):
        self.screen = screen
        self.velocity = 5

        # load bmp image and get rectangle
        image_random = random.randint(1, len(self.images))
        self.image = pg.image.load(self.images[image_random - 1])
        len_random = random.randint(10, 80)
        self.image = pg.transform.scale(self.image, (len_random, len_random))
        self.rect = self.image.get_rect() # asteroid real size

        self.screen_rect = screen.get_rect()

        #put asteroid on the right side of window
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

    #def randomize(self):
        

    def create(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        if self.rect.right + self.velocity > self.screen_rect.left:
            self.rect.right -= self.velocity
        else:
            self.rect.right = self.screen_rect.right

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

    """
    def aparicion(self):
        for i in range (random.randint(2)):
            radio = random.randint(5, 14)
            self.asteroid.append(Asteroid(random.randint(radio, ancho - radio),
                                    random.randint(radio, alto - radio),
                                    self.pantalla, 
                                    (random.randint(0,255),
                                     random.randint(0,255),
                                     random.randint(0,255)),
                                     radio))
            self.asteroid[i].vx = random.randint(5,15) * random.choice[(-1, 1)] 
    """    
