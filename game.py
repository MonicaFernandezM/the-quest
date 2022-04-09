import pygame as pg
from ship import Ship 
from asteroid import Asteroid

class Game():
    def __init__(self, screen):
        self.lives = 3
        self.game_time = 60 # 60 seconds
        self.screen = screen
        self.ship = Ship(self.screen)
        self.asteroids = [
            Asteroid(self.screen), 
            Asteroid(self.screen),
            Asteroid(self.screen)]

    # Handling user's events    
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or ( 
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                pg.quit()

    # Handling screen setup
    def setup_screen(self):
        image = pg.image.load('images/polar-lights-ga4cf63a15_1920.jpg')
        self.screen.blit(image, (0,0))
        
        self.ship.create()
        self.ship.move()
        for asteroid in self.asteroids:
            asteroid.create()
            asteroid.move()
        pg.display.flip()

    # Handling game duration and user lives
    def decrease_life(self):
        self.lives -= 1
        if self.lives == 0:
            print("Game Over")
    
    # Handling game structure
    def game_control(self):
        self.check_intersection()
        self.create_asteroids()

    def check_intersection(self):
        for asteroid in self.asteroids:
            if asteroid.intersection(self.ship):
                self.asteroids.remove(asteroid)
                #asteroid.remove()
                self.decrease_life()

    def create_asteroids(self):
        if len(self.asteroids) < 20:
            self.asteroids.append(Asteroid(self.screen))
