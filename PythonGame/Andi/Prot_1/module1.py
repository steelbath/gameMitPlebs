import pygame as pg
import numpy as np
from andi_classes import *



def mobs_create(mob_number):
    enemy = pg.image.load("enemy sprite slurp.png")
    #get all mobs into a list
    mobs_list = []
    mobs  = np.zeros((mob_number,3,2))
    for i in np.arange(mob_number):
        mobs_list.append(Enemies(enemy,[np.random.randint(-10,10), np.random.randint(-10,10)],[np.random.randint(0,1280),np.random.randint(0,720)]))
        mobs[i,0] = mobs_list[i].topleft
        mobs[i,1] = mobs_list[i].bottomright
        mobs[i,2] = mobs_list[i].pos
        
    return mobs,mobs_list




def mobs_collide(mob_number, mobs, mobs_list, screen):
    for i,mob in enumerate(mobs_list):
        screen.blit(mobs_list[i].image, ((int(mobs[i,2,0]), int(mobs[i,2,1]))))
        
        mobs[i,0] = mobs_list[i].topleft
        mobs[i,1] = mobs_list[i].bottomright
        mobs[i,2] = mobs_list[i].pos
        
    
        
        for m in np.arange(mob_number):
            if not m==i:
                
                
                if mobs[i,0,0] <= mobs[m,1,0] and mobs[i,0,1] <= mobs[m,1,1] and mobs[i,1,0] >= mobs[m,1,0] and mobs[i,1,1] >= mobs[m,1,1]:
                    
                    mob.collision()
                    
                elif mobs[i,1,0] >= mobs[m,0,0] and mobs[i,1,1] >= mobs[m,0,1] and mobs[i,0,0] <= mobs[m,0,0] and mobs[i,0,1] <= mobs[m,0,1]:
                    
                    mob.collision()

        mobs_list[i].move()
    return mobs



def mobs_collision(mob_number,mobs_list, screen):

    mobs_pos_list = [0]*(mob_number)

    #define an array where the collisions get saved
    mob_collided_array = np.zeros((mob_number))

    #enumerate over all mobs in the mobs list
    for index, mob in enumerate(mobs_list): 

        #Getting the rectangles from the Enemies after moving
        mobs_pos_list[index] = np.array(mob.move())

        #define a new array for calculation
        mobs_zeros = np.array([pg.Rect(0,0,0,0)]*(mob_number))

        #blit the mobs movement


        screen.blit(mob.image, mob.rect) 
    
    
    
    for index, mob in enumerate(mobs_list):
        
        mobs_zeros[index] = mobs_pos_list[index]

        #getting an array without the rectangle that is indexed in that step
        mobs_collision_list = mobs_pos_list-mobs_zeros
        mob_collided_array[index] = pg.Rect(mobs_pos_list[index]).collidelist(mobs_collision_list)
        
        #setting the mobs_zeros array zero again for the next index
        mobs_zeros[index] = pg.Rect(0,0,0,0)
        
        
        #checking if the Rect[index] is colliding with something
        if not mob_collided_array[index] == -1:
        #changeing the speed of the mob by the Enemies.collision() method  
            mob.collision()          

    return mobs_list
