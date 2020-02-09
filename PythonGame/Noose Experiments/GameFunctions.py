import pygame as pg
import sys

def check_events(P1):
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                P1.pressedkeys[0]=True
            if event.key == pg.K_LEFT:
                P1.pressedkeys[1]=True
            if event.key == pg.K_DOWN: 
                P1.pressedkeys[2]=True
            if event.key == pg.K_RIGHT:
                P1.pressedkeys[3]=True
        if event.type == pg.KEYUP:
           if event.key == pg.K_RIGHT:
                P1.pressedkeys[3]=False
           if event.key == pg.K_LEFT:
               P1.pressedkeys[1]=False
           if event.key == pg.K_UP: 
               P1.pressedkeys[0]=False
           if event.key == pg.K_DOWN:
               P1.pressedkeys[2]=False


def update_screen(GS, screen, P1):
    screen.fill(GS.bg_color)
    P1.blitme()    

    
    pg.display.flip()