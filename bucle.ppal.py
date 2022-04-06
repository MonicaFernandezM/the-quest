import pygame as pg
from game import Game

def run_game():
    pg.init()
    FPS = 60
    clock = pg.time.Clock()
    screen = pg.display.set_mode((1000, 750)) #1300, 750
    pg.display.set_caption("The Quest")
    game = Game(screen)

    while True:
        clock.tick(FPS)
        game.check_events()
        game.setup_screen()

run_game()
