import pygame as pg
from game import Game
from settings import Settings

def run_game():
    pg.init()
    clock = pg.time.Clock()
    screen = pg.display.set_mode((Settings().screen_width, Settings().screen_height)) 
    pg.display.set_caption("The Quest")
    game = Game(screen)

    while True:
        clock.tick(Settings().FPS)
        game.check_events()
        game.setup_screen()
        game.game_control()

run_game()
