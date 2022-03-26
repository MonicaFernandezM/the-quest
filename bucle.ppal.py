import sys
import pygame as pg
from theQuest import Ship, Asteroid 

pg.init 

def run_game():
    screen = pg.display.set_mode((1300, 750))
    ship = Ship(screen)
    asteroid = Asteroid(screen)
    pg.display.set_caption("The Quest")

    while True:
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                sys.exit()

        screen.fill((127, 255, 212))
        ship.create()
        asteroid.create()
        pg.display.flip()

run_game()

