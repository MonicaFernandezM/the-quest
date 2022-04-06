import pygame as pg
from ship import Ship 
from asteroid import Asteroid

class Game():
    def __init__(self, screen):
        self.lives = 3
        self.screen = screen
        self.ship = Ship(self.screen)
        self.asteroid = Asteroid(self.screen)

    def decrease_life(self):
        self.lives -= 1
        if self.lives == 0:
            print("Game Over")
        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or ( 
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()
        
    def setup_screen(self):
        image = pg.image.load('images/milky-way-g2b03805d6_1920.jpg')
        self.screen.blit(image, (0,0))
        self.ship.create()
        self.asteroid.create()
        self.ship.move()
        self.asteroid.move()
        pg.display.flip()
    
        if self.asteroid.intersection(self.ship):
            #self.asteroid.image.fill((0, 0, 0, 0))
            self.asteroid.remove()
            self.decrease_life()
