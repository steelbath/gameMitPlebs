import pygame as pg
import numpy as np
from andi_classes import *



def mobs_create(mob_number):
    enemy = pg.image.load("enemy sprite slurp.png")
    #get all mobs into a list
    mobs_list = []
    mobs  = np.zeros((mob_number,3,2))
    for i in np.arange(mob_number):
        mobs_list.append(Enemies(enemy,[np.random.randint(-10,10), np.random.randint(-10,10)],[np.random.randint(0,1024),np.random.randint(0,768)]))
        mobs[i,0] = mobs_list[i].topleft
        mobs[i,1] = mobs_list[i].bottomright
        mobs[i,2] = mobs_list[i].pos
        
    return mobs,mobs_list




def mobs_collide(mob_number, mobs_coordinates, mobs_list, screen):
    for i,mob in enumerate(mobs_list):
        
        screen.blit(mobs_list[i].image, ((int(mobs_coordinates[i,2,0]), int(mobs_coordinates[i,2,1]))))
        
        mobs_coordinates[i,0] = mobs_list[i].topleft
        mobs_coordinates[i,1] = mobs_list[i].bottomright
        mobs_coordinates[i,2] = mobs_list[i].pos
        
    
        
        for m in np.arange(mob_number):
            if not m==i:
             
                if mobs_coordinates[i,0,0] <= mobs_coordinates[m,1,0] and mobs_coordinates[i,0,1] <= mobs_coordinates[m,1,1] and mobs_coordinates[i,1,0] >= mobs_coordinates[m,1,0] and mobs_coordinates[i,1,1] >= mobs_coordinates[m,1,1]:
                    
                    mob.collision()
                    
                elif mobs_coordinates[i,1,0] >= mobs_coordinates[m,0,0] and mobs_coordinates[i,1,1] >= mobs_coordinates[m,0,1] and mobs_coordinates[i,0,0] <= mobs_coordinates[m,0,0] and mobs_coordinates[i,0,1] <= mobs_coordinates[m,0,1]:
                    
                    mob.collision()
        
        mob.move()
        
        
    return mobs_coordinates





  
