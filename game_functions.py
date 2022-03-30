import sys
import pygame as pg
from ship import Direction

def check_events(ship):
        # Watch for keyboard and mouse events.
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                ship.move(Direction.UP)
            elif event.key == pg.K_DOWN:
                ship.move(Direction.DOWN)
            

def update_screen(screen, ship, asteroid):

    screen.fill((127, 255, 212))
    ship.create()
    asteroid.create()
    pg.display.flip()