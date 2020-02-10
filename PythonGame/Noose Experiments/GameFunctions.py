import pygame as pg
import sys
import numpy as np
 


#Game Variables
projectiles = np.zeros((100,4),dtype=int)
#pmap[1]=pointer pmap[2]=length
pmap = np.zeros(101,dtype=int)

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
                P1.shoot(P1.direction,P1.pos)
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
    print(projectiles[0])
    for i in range(0, 90):
        if [projectiles[i,0], projectiles[i,1]] != [0,0]:            
            pg.draw.rect(screen, (150,50,50), (projectiles[i,0], projectiles[i,1],5,5))
            projectiles[i,0]+=projectiles[i,2]
            projectiles[i,1]+=projectiles[i,3]
            if projectiles[i,0] > 1024 or projectiles[i,0] < 0 or projectiles[i,1] > 768 or projectiles[i,1] <0:
                projectiles[i,0] = 0
                projectiles[i,1] = 0


    
    pg.display.flip()