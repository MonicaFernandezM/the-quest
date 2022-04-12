import pygame as pg
from ship import Ship 
from asteroid import Asteroid
from settings import Settings
import time 

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
        self.clock = pg.time.Clock()

    # Handling screen setup
    def setup_screen(self):
        self.bg_image = pg.image.load(Settings().background_image)
        self.bg_rect = self.bg_image.get_rect()
        self.screen.blit(self.bg_image, self.bg_rect)

        self.level_punctuation = self.font.render("Punctuation: " + str(self.punctuation), True, (255, 255, 255))        
        self.level_text = self.font.render("Level: " + str(1), True, (255, 255, 255))        
        self.life_text = self.font.render("Lives: " + str(self.lives), True, (255, 255, 255))
        self.screen.blit(self.level_punctuation, (10,10))
        self.screen.blit(self.level_text, (Settings().screen_width / 4, 10))
        self.screen.blit(self.life_text, (Settings().screen_width / 2, 10))

        self.ship.create()
        self.ship.move()
        for asteroid in self.asteroids:
            asteroid.create()
            asteroid.move()
        pg.display.flip()

    # Handling game duration and user lives
    def decrease_life(self):
        if self.lives - 1 > -1:
            self.lives -= 1
        elif self.lives - 1 == -1:
            print("Game Over")
            self.show_explosion()
    
    # Handling game structure
    def game_control(self):
        self.check_intersection()
        self.check_reached_end()
        self.create_asteroids()
        self.show_time()

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

    def show_explosion(self):
        print("Explosion")
        self.explosion_image = pg.image.load('images/icons8-flash-bang-48.png')
        self.rect = self.explosion_image.get_rect()
        self.rect.centerx = self.ship.rect.right
        self.rect.centery = self.ship.rect.centery
        self.screen.blit(self.explosion_image, self.rect)
        pg.display.flip()
        
    def show_time(self):
        self.clock.tick(60)
        self.the_time = time.strftime("%S", time.localtime())
        self.time_text = self.font.render("Time: " + self.the_time, True, (255, 255, 255))
        self.screen.blit(self.time_text, (Settings().screen_width * 3 / 4, 10))
        pg.display.update()