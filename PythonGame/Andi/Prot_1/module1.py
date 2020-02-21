import pygame as pg
import numpy as np
from andi_classes import *



def mobs_create(mob_number):
    enemy = pg.image.load("enemy sprite slurp.png")
    #get all mobs into a list
    mobs_list = []
    mobs  = np.zeros((mob_number,6,2))
    for i in np.arange(mob_number):
        mobs_list.append(Enemies(enemy,[np.random.randint(-10,10), np.random.randint(-10,10)],[np.random.randint(0,1024),np.random.randint(0,768)]))
        mobs[i,0] = mobs_list[i].topleft
        mobs[i,1] = mobs_list[i].bottomright
        mobs[i,2] = mobs_list[i].pos
        mobs[i,3] = mobs_list[i].speed
        mobs[i,4,0] = mobs_list[i].left
        mobs[i,4,1] = mobs_list[i].right
        mobs[i,5,0] = mobs_list[i].top
        mobs[i,5,1] = mobs_list[i].bottom
        
    return mobs,mobs_list




def mobs_collide(mob_number, mobs_coordinates, mobs_list, screen):
    mob_speed_total = np.zeros((mob_number,mob_number,2))
    for i,mob_1 in enumerate(mobs_list):
        
       
        screen.blit(mobs_list[i].image,mobs_list[i].rect)
        
        mobs_coordinates[i,0] = mobs_list[i].topleft
        mobs_coordinates[i,1] = mobs_list[i].bottomright
        mobs_coordinates[i,2] = mobs_list[i].pos
        mobs_coordinates[i,3] = mobs_list[i].speed
        mobs_coordinates[i,4,0] = mobs_list[i].left
        mobs_coordinates[i,4,1] = mobs_list[i].right
        mobs_coordinates[i,5,0] = mobs_list[i].top
        mobs_coordinates[i,5,1] = mobs_list[i].bottom
            
        
        for m in np.arange(mob_number):
            if not m==i:
                if mobs_coordinates[i,4,0] <= mobs_coordinates[m,4,1] and mobs_coordinates[i,4,0] >= mobs_coordinates[m,4,0]:
                    if mobs_coordinates[i,5,0] <= mobs_coordinates[m,5,0] and mobs_coordinates[i,5,1] >= mobs_coordinates[m,5,0]:
                        mob_speed_total[i,m] = mob_1.collision(mobs_coordinates[m,3])
                    elif mobs_coordinates[i,5,0] <= mobs_coordinates[m,5,1] and mobs_coordinates[i,5,1] >= mobs_coordinates[m,5,1]:
                        mob_speed_total[i,m] = mob_1.collision(mobs_coordinates[m,3])
                elif mobs_coordinates[i,4,1] >= mobs_coordinates[m,4,0] and mobs_coordinates[i,4,1] <= mobs_coordinates[m,4,1]:
                    if mobs_coordinates[i,5,0] <= mobs_coordinates[m,5,0] and mobs_coordinates[i,5,1] >= mobs_coordinates[m,5,0]:
                        mob_speed_total[i,m] = mob_1.collision(mobs_coordinates[m,3])
                    elif mobs_coordinates[i,5,0] <= mobs_coordinates[m,5,1] and mobs_coordinates[i,5,1] >= mobs_coordinates[m,5,1]:
                        mob_speed_total[i,m] = mob_1.collision(mobs_coordinates[m,3])

            #if not m==i:
            # 
            #    if mobs_coordinates[i,0,0] <= mobs_coordinates[m,1,0] and mobs_coordinates[i,0,1] <= mobs_coordinates[m,1,1] and mobs_coordinates[i,1,0] >= mobs_coordinates[m,1,0] and mobs_coordinates[i,1,1] >= mobs_coordinates[m,1,1]:
            #        
            #            mob_speed_total[i,m] = mob_1.collision(mobs_coordinates[m,3])
            #        
            #        
            #    elif mobs_coordinates[i,1,0] >= mobs_coordinates[m,0,0] and mobs_coordinates[i,1,1] >= mobs_coordinates[m,0,1] and mobs_coordinates[i,0,0] <= mobs_coordinates[m,0,0] and mobs_coordinates[i,0,1] <= mobs_coordinates[m,0,1]:
            #        
            #            mob_speed_total[i,m] = mob_1.collision(mobs_coordinates[m,3])
        
        if not mob_speed_total[i].all() == 0:
            mobs_list[i].speed = np.sum(mob_speed_total, axis = 1)[i]
          
        mob_1.move()
        
        
        
    return mobs_coordinates





  
