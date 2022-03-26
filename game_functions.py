import sys
import pygame as pg

def check_events():
    #respond to  keyboard and mouse item
    for event in pg.event.get():
        if event.type == pg.QUIT:
            sys.exit()