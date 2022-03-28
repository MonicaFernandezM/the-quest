import sys
import pygame as pg


def check_events():
    #respond to  keyboard and mouse item
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()

def update_screen(ai_settings,screen,ship):
    # fill color
    screen.fill(ai_settings.bg_color)
    ship.create()
    # visualiaze the window
    pg.display.flip()

#function is refactored
def check_keydown_events(event,ship):
    if event.key == pg.K_UP:
    #move up
        ship.moving_up = True
    elif event.key == pg.K_DOWN:
    #move down
        ship.moving_down = True 

def check_keyup_events(event,ship):
    if event.key == pg.K_UP:
        ship.moving_up = False
    elif event.key == pg.K_DOWN:
        #move up
        ship.moving_down = False
def check_events(ship):
    #respond to  keyboard and mouse item
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()
        elif event.type == pg.KEYDOWN:
            check_keydown_events(event,ship)
        elif event.type == pg.KEYUP:
            check_keyup_events(event,ship)
