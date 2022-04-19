import pygame as pg
from ship import Ship 
from asteroid import Asteroid
from settings import Settings
import time 
from enum import Enum
import random

class Level(Enum):
    One = 1
    Two = 2
    Three = 3

class Result(Enum):
    Nothing = 1
    Win = 2
    Lose = 3

class Game():
    def __init__(self, screen, level):
        self.settings = Settings()
        pg.mixer.init()
        pg.mixer.music.load(self.settings.music_explotion)
        self.seconds = 0
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ship = Ship(self.screen)
        self.max_time = self.settings.max_game_time
        self.font = pg.font.Font(None, 30)
        self.punctuation = 0
        self.lives = self.settings.lives
        self.game_result  = Result.Nothing
        self.start_ticks = pg.time.get_ticks() #starter tick
        self.avoided_asteroid = 0
        
        if level == Level.One:
            self.max_asteroids = self.settings.max_asteroid_one
            self.asteroids = [Asteroid(self.screen)]
            self.bg_image = pg.image.load(self.settings.background_image_level_one)
            self.velocity = random.randint(self.settings.min_asteorid_velocity_level_one, self.settings.max_asteroid_velocity_level_one)
            
        elif level == Level.Two:
            self.max_asteroids = self.settings.max_asteroid_two
            self.asteroids = [
                Asteroid(self.screen), 
                Asteroid(self.screen)]
            self.bg_image = pg.image.load(self.settings.background_image_level_two)
            self.velocity = random.randint(self.settings.min_asteorid_velocity_level_two, self.settings.max_asteroid_velocity_level_two)
        elif level == Level.Three:
            self.max_asteroids = self.settings.max_asteroid_three
            self.asteroids = [
                Asteroid(self.screen), 
                Asteroid(self.screen),
                Asteroid(self.screen)]
            self.bg_image = pg.image.load(self.settings.background_image_level_three)
            self.velocity = random.randint(self.settings.min_asteorid_velocity_level_three, self.settings.max_asteroid_velocity_level_three)

        self.bg_rect = self.bg_image.get_rect()

    # Handling screen update
    def update_screen(self):
        self.screen.blit(self.bg_image, self.bg_rect)
        self.punctuation_text = self.font.render("Punctuation: " + str(self.punctuation), True, (255, 255, 255))
        self.level_text = self.font.render("Level: " + str(1), True, (255, 255, 255))        
        self.life_text = self.font.render("Lives: " + str(self.lives), True, (255, 255, 255))
        self.time_text = self.font.render("Time: " + str(int(self.max_time - self.seconds)), True, (255, 255, 255))

        self.screen.blit(self.punctuation_text, (10, 10))
        self.screen.blit(self.level_text, (self.settings.screen_width / 4, 10))
        self.screen.blit(self.life_text, (self.settings.screen_width / 2, 10))
        self.screen.blit(self.time_text, (self.settings.screen_width * 3 / 4, 10))

        if self.game_result == Result.Nothing:
            self.ship.create()
            self.ship.move()

            for asteroid in self.asteroids:
                asteroid.create()
                asteroid.move()

        elif self.game_result == Result.Lose:
            self.show_explosion()
        
        elif self.game_result == Result.Win:
            self.draw_planet()
            self.ship.rotate_ship(180)
            pg.time.wait(260)

        pg.display.update()

    # Handling game duration and user lives
    def decrease_life(self):
        if self.lives - 1 > -1:
            self.lives -= 1
        elif self.lives - 1 == -1:
            self.game_result = Result.Lose
    
    # Handling game structure
    def game_control(self):
        self.check_intersection()
        self.check_reached_end()
        self.create_asteroids()
        self.show_time()
        #self.check_asteroids_avoided()

    def check_intersection(self):
        for asteroid in self.asteroids:
            if asteroid.intersection(self.ship):
                self.asteroids.remove(asteroid)
                self.decrease_life()
    
    def check_reached_end(self):
        for asteroid in self.asteroids:
            if asteroid.reached_end():
                self.asteroids.remove(asteroid)
                self.punctuation += asteroid.value

    def create_asteroids(self):
        if len(self.asteroids) < self.max_asteroids:
            self.asteroids.append(Asteroid(self.screen))

    def show_explosion(self):
        self.explosion_image = pg.image.load('images/icons8-flash-bang-48.png')
        self.explosion_rect = self.ship.rect
        self.explosion_rect.centerx = self.ship.rect.centerx
        self.explosion_rect.centery = self.ship.rect.centery
        self.screen.blit(self.explosion_image, self.explosion_rect)
        pg.mixer.music.play()
        pg.mixer.music.set_volume(0.6)

    def show_time(self):
        if self.game_result == Result.Nothing:
            self.seconds = (pg.time.get_ticks() - self.start_ticks) / 1000
            if self.seconds >= self.max_time:
                self.game_result = Result.Win

    def draw_planet(self):
        planet_rect = self.screen_rect
        planet_rect.centerx = self.screen_rect.width * 4 / 3    
        pg.draw.circle(self.screen, (235, 205, 124), (planet_rect.centerx, planet_rect.centery), self.screen_rect.width / 2)
        pg.draw.circle(self.screen, (240, 212, 139), (planet_rect.centerx + 25, planet_rect.centery), self.screen_rect.width / 2)
    
    """ End condition when avoided x number of asteroids 
    def check_asteroids_avoided(self):
        if self.avoided_asteroid > 5:
            self.game_result = Result.Win
    """