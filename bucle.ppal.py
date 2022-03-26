import sys
import pygame as pg
from ship import Ship 
from asteroid import Asteroid
import game_functions as gf

def run_game():
    pg.init()
    screen = pg.display.set_mode((1300, 750))
    ship = Ship(screen)
    asteroid = Asteroid(screen)
    pg.display.set_caption("The Quest")

    while True:
        gf.check_events()
        screen.fill((127, 255, 212))
        ship.create()
        asteroid.create()
        pg.display.flip()

run_game()

