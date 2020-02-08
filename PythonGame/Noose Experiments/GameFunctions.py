import pygame as pg
import sys

def check_events(P1):
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            sys.exit()

    accel=0.01

    pressed=pg.key.get_pressed()
    if pressed[pg.K_RIGHT]:
        if P1.speed[0] < 1:
            P1.speed[0]+=accel
    elif P1.speed[0] > 0:
        P1.speed[0]-=accel
    if pressed[pg.K_LEFT]:
        if P1.speed[0] > -1:
            P1.speed[0]-=accel
    elif P1.speed[0] > 0:
        P1.speed[0]+=accel
    if pressed[pg.K_UP]:
        if P1.speed[1] > -1:
            P1.speed[1]-=accel
    elif P1.speed[1] > 0:
        P1.speed[1]+=accel
    if pressed[pg.K_DOWN]:
        if P1.speed[1] < 1:
            P1.speed[1]+=accel
    elif P1.speed[1] > 0:
        P1.speed[1]-=accel

def update_screen(GS, screen, P1):
    screen.fill(GS.bg_color)
    P1.blitme()    

    
    pg.display.flip()