import pygame as pg
import sys

def check_events(P1):
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()


        accel = 0.01
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RIGHT:
                if P1.speed[0] < 1:
                    P1.speed[0]+=accel
            if event.key == pg.K_LEFT:
                if P1.speed[0] > -1:
                    P1.speed[0]-=accel
            if event.key == pg.K_UP: 
                if P1.speed[1] > -1:
                    P1.speed[1]-=accel
            if event.key == pg.K_DOWN:
                if P1.speed[1] < 1:
                    P1.speed[1]+=accel
  #      if event.type == pg.KEYUP:
 #           if event.key == pg.RIGHT:
#                decelL


def update_screen(GS, screen, P1):
    screen.fill(GS.bg_color)
    P1.blitme()    

    
    pg.display.flip()