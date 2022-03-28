import sys
import pygame as pg
from ship import Ship 
from asteroid import Asteroid
import game_functions as gamef
from settings import Settings

def run_game():
    pg.init()
    ai_settings = Settings()
    screen = pg.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    asteroid = Asteroid(screen)
    pg.display.set_caption("The Quest")
    
    
    while True:
        #supervise keyboard and mouse item 
        gamef.check_events()
        gamef.update_screen(ai_settings, screen, ship)
        #screen.fill(sc_settings.bg_color)
        #ship.create()
        #asteroid.create()
        #pg.display.flip()

run_game()

