import sys
import pygame as pg
from ship import Ship 
from asteroid import Asteroid
import game_functions as gamef

def run_game():
    pg.init()

    screen = pg.display.set_mode((1000, 750)) #1300, 750
    ship = Ship(screen)
    asteroid = Asteroid(screen)

    pg.display.set_caption("The Quest")
    
    while True:
        gamef.check_events(ship)
        gamef.update_screen(screen, ship, asteroid)

run_game()
