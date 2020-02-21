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


#collision map:type, index
cmap = np.zeros((768,1024,2),dtype=int)


def bullethit(ma,i,bspeed):
    ma[i].speed[0]=ma[i].speed[0]+bspeed[0]/10  
    ma[i].speed[1]=ma[i].speed[1]+bspeed[1]/10
#types = 0 empty 1 mob 2 player 3 bullet 
#ma=mobarray
def render_bullets(screen,P1,ma):
    for i in range(0,99):
        if [P1.projectiles[i,0],P1.projectiles[i,1]] != [0,0]:
            cmap[P1.projectiles[i,1],P1.projectiles[i,0],0]=0
            P1.projectiles[i,0]+=P1.projectiles[i,2]
            P1.projectiles[i,1]+=P1.projectiles[i,3]            
            if P1.projectiles[i,0] >= 1023 or P1.projectiles[i,0] <=0 or  P1.projectiles[i,1] >= 767 or P1.projectiles[i,1] <= 0:
                P1.projectiles[i,0] = 0
                P1.projectiles[i,1] = 0
            elif cmap[int(P1.projectiles[i,1]),int(P1.projectiles[i,0]),0] != 1:       
                cmap[P1.projectiles[i,1],P1.projectiles[i,0],0]=3
                pg.draw.rect(screen, (150,50,50), ( P1.projectiles[i,0],  P1.projectiles[i,1],5,5))
            else:
                index = cmap[P1.projectiles[i,1], P1.projectiles[i,0],1]
                bullethit(ma,index-1,[P1.projectiles[i,2],P1.projectiles[i,3]])
                P1.projectiles[i,0] = 0
                P1.projectiles[i,1] = 0



def update_screen(GS, screen, P1,mobarray):
    screen.fill(GS.bg_color)
    P1.blitme()
    render_bullets(screen, P1,mobarray)
    mobarray[0].blitme()
    for i in range(0,3):
        mobarray[i].blitme()

    pg.display.flip()
