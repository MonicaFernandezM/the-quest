import pygame as pg

def check_events(ship):
    for event in pg.event.get():
        if event.type == pg.QUIT or ( 
            event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
        ):
            pg.quit()
        
def setup_screen(screen, ship, asteroid):
    # screen.fill((127, 255, 212))
    image = pg.image.load('images/milky-way-g2b03805d6_1920.jpg')
    screen.blit(image, (0,0))
    ship.create()
    asteroid.create()
    pg.display.flip()