import pygame as pg
import sys

#compare signns
def csign(a,b):
    return a >= 0 and b >= 0 or a < 0 and b < 0

def check_events(P1):
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()
        

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                P1.direction[1]-=1
            if event.key == pg.K_LEFT:
                P1.direction[0]-=1
            if event.key == pg.K_DOWN: 
                P1.direction[1]+=1
            if event.key == pg.K_RIGHT:
                P1.direction[0]+=1
        if event.type == pg.KEYUP:
           if event.key == pg.K_UP:
                P1.direction[1]+=1
           if event.key == pg.K_LEFT:
               P1.direction[0]+=1
           if event.key == pg.K_DOWN: 
               P1.direction[1]-=1
           if event.key == pg.K_RIGHT:
               P1.direction[0]-=1


def update_screen(GS, screen, P1):
    screen.fill(GS.bg_color)
    P1.blitme()    

    
    pg.display.flip()