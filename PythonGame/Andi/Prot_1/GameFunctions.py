import pygame as pg
import sys
import numpy as np

#compare signs
def csign(a,b):
    return a >= 0 and b >= 0 or a < 0 and b < 0

def check_events(P1):
    
    
    running = True
    for event in pg.event.get():
        

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
                #updating the counter

                P1.event_number += 1
                P1.projectiles[P1.event_number] = P1.pos

                #assining the projectiles coordinates [x,y,length,height] to the array
                #the index is given by the event_number counter
               
                
                if P1.event_number == 70:
                    P1.event_number = -1
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
        
    return np.array([P1.projectiles, P1.event_number, running, P1.pos])

def update_screen(GS, screen, P1):
    screen.fill(GS.bg_color)
    P1.blitme()    

    
    pg.display.flip()