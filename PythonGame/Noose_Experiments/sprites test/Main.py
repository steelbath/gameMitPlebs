import sys
import pygame as pg

from classfile import *
import GameFunctions as gf

Clock = pg.time.Clock()

def game():
    pg.init()
    GS = GameSettings()
    screen= pg.display.set_mode((GS.screen_width,GS.screen_height))
    pg.display.set_caption("Shootnshit")


    Player1 = Player(screen, pg.image.load("Spielfigur.png").convert(), (500,500),(0,0))

    while True:
        gf.check_events(Player1)
        Player1.checkKeys()
        Player1.update()
        bullets.update()
        gf.update_screen(GS, screen, Player1,bullets) 

        Clock.tick(120)

game()
