import pygame as pg
import sys

#compare signs true if same
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
            if event.key == pg.K_SPACE:
                P1.shoottickcount=0
                P1.shooting=1
            if event.key == pg.K_ESCAPE:
                sys.exit()
        if event.type == pg.KEYUP:
           if event.key == pg.K_UP:
                P1.direction[1]+=1
           if event.key == pg.K_LEFT:
               P1.direction[0]+=1
           if event.key == pg.K_DOWN: 
               P1.direction[1]-=1
           if event.key == pg.K_RIGHT:
               P1.direction[0]-=1
           if event.key == pg.K_SPACE:
               P1.shooting=0

def render_bullets(screen, P1):
    for i in range(0,99):
        if [P1.projectiles[i,0], P1.projectiles[i,1]] != [0,0]:
            pg.draw.rect(screen, (150,50,50), (P1.projectiles[i,0], P1.projectiles[i,1],5,5))
            P1.projectiles[i,0]+=P1.projectiles[i,2]
            P1.projectiles[i,1]+=P1.projectiles[i,3]

def update_screen(GS, screen, P1):
    screen.fill(GS.bg_color)
    P1.blitme()
    render_bullets(screen, P1)
    pg.display.flip()
