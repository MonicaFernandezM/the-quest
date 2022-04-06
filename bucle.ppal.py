import sys
import pygame as pg
from ship import Ship 
from asteroid import Asteroid
import game_functions as gamef

def run_game():
    pg.init()
    FPS = 60
    clock = pg.time.Clock()
    screen = pg.display.set_mode((1000, 750)) #1300, 750
    pg.display.set_caption("The Quest")
    ship = Ship(screen)
    asteroid = Asteroid(screen)

    while True:
        clock.tick(FPS)
        gamef.check_events(ship)
        gamef.setup_screen(screen, ship, asteroid)
        ship.move()
        asteroid.move()

run_game()
