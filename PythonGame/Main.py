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
    mobcount = 3
    mobarray = [0]*mobcount
    for i in range(0,mobcount):
        print(i)
        x=np.random.randint(20,1004)
        y=np.random.randint(20,748)
        mobarray[i]=testmob(i,screen, pg.image.load("goomba enemy.png").convert(),[x,y],[2,0])
  
    while True:
        gf.check_events(Player1)
        Player1.checkKeys()
        Player1.update()
        for i in range(0,mobcount):
            mobarray[i].update()
        gf.update_screen(GS, screen, Player1,mobarray) 
        Clock.tick(120)

game()
