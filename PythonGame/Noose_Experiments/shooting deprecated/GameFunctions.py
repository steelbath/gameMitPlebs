import pygame as pg
import sys
import numpy as np
 



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
                P1.shoot(P1.facing,P1.pos)
            if event.key == pg.K_ESCAPE:
                running = False
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
    for i in range(0, P1.pindex['lb']):
        if [P1.projectiles[i,0], P1.projectiles[i,1]] != [0,0]:            
            pg.draw.rect(screen, (150,50,50), (P1.projectiles[i,0], P1.projectiles[i,1],5,5))
            P1.projectiles[i,0]+=P1.projectiles[i,2]
            P1.projectiles[i,1]+=P1.projectiles[i,3]
            #bullet collided 
            if P1.projectiles[i,0] > 1024 or P1.projectiles[i,0] < 0 or P1.projectiles[i,1] > 768 or P1.projectiles[i,1] <0:
               if i != P1.pindex['lb']:
                   P1.pindex['le'] += 1
                   P1.pmap[P1.pindex['le']] = i
               else:
                   P1.pindex['lb']-=1
               P1.projectiles[i,0] = 0
               P1.projectiles[i,1] = 0


    
    pg.display.flip()