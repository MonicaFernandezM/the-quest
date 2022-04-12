
import pygame as pg
from ship import Ship 
from asteroid import Asteroid
from settings import Settings

class Game():
    def __init__(self, screen):
        self.screen = screen
        self.ship = Ship(self.screen)
        self.asteroids = [
            Asteroid(self.screen), 
            Asteroid(self.screen),
            Asteroid(self.screen)]
        self.font = pg.font.Font(None, 30)
        self.punctuation = 0
        self.lives = Settings().lives

    # Handling screen setup
    def setup_screen(self):
        image = pg.image.load(Settings().background_image)
        self.screen.blit(image, (0, 0))

        self.level_punctuation = self.font.render("Punctuation: " + str(self.punctuation), True, (255, 255, 255))        
        self.level_text = self.font.render("Level: " + str(1), True, (255, 255, 255))        
        self.life_text = self.font.render("Lives: " + str(self.lives), True, (255, 255, 255))
        self.time_text = self.font.render("Time: " + str(60), True, (255, 255, 255))
        self.screen.blit(self.level_punctuation, (10,10))
        self.screen.blit(self.level_text, (Settings().screen_width / 4, 10))
        self.screen.blit(self.life_text, (Settings().screen_width / 2, 10))
        self.screen.blit(self.time_text, (Settings().screen_width * 3 / 4, 10))

        self.ship.create()
        self.ship.move()
        for asteroid in self.asteroids:
            asteroid.create()
            asteroid.move()
        pg.display.flip()

    # Handling game duration and user lives
    def decrease_life(self):
        if self.lives - 1 >= 0:
            self.lives -= 1
            print("Game Over")
    
    # Handling game structure
    def game_control(self):
        self.check_intersection()
        self.check_reached_end()
        self.create_asteroids()

    def check_intersection(self):
        for asteroid in self.asteroids:
            if asteroid.intersection(self.ship):
                self.asteroids.remove(asteroid)
                self.decrease_life()
    
    def check_reached_end(self):
        for asteroid in self.asteroids:
            if asteroid.reached_end():
                self.asteroids.remove(asteroid)
                self.punctuation += 10

    def create_asteroids(self):
        if len(self.asteroids) < Settings().max_asteroid:
            self.asteroids.append(Asteroid(self.screen))
