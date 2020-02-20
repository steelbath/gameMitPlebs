import sys
import pygame as pg


from Noose_Experiments.classfile import *
import Noose_Experiments.GameFunctions as gf
from Noose_Experiments.GameClass import *

Clock = pg.time.Clock()

def game():
    pg.init()
    GS = GameSettings()
    screen= pg.display.set_mode((GS.screen_width,GS.screen_height))
    pg.display.set_caption("Shootnshit")

    Player1 = Player(screen, pg.image.load("Spielfigur.png").convert(), (500,500),(0,0))
    Game.setup_states({'state1','state2'},'state1')
    while True:
        gf.check_events(Player1)
        Player1.checkKeys()
        Player1.update()
        gf.update_screen(GS, screen, Player1) 

        Clock.tick(5)

game()
