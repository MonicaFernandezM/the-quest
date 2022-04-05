import pygame as pg

def check_events(ship):
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
        
def setup_screen(screen, ship, asteroid):
    screen.fill((127, 255, 212))
    ship.create()
    asteroid.create()
    pg.display.flip()
