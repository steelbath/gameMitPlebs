import sys
import pygame as pg

from classfile import *
import GameFunctions as gf

Clock = pg.time.Clock()

def game():
    pg.init()
    GO = GameObject()
    screen= pg.display.set_mode((GO.screen_width,GO.screen_height))
    pg.display.set_caption("Shootnshit")
    running = True
    Player1 = Player(screen, pg.image.load("Spielfigur.png").convert(), (500,500),(0,0))
  

    while running:
        gf.check_events(Player1)
        Player1.checkKeys()
        Player1.update()
        gf.update_screen(GO, screen, Player1) 

        Clock.tick(120)

game()