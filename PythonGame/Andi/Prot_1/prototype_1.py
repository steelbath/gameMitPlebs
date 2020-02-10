import numpy as np
import pygame as pg
from classes import * 
from classfile import *
import GameFunctions as gf


Clock = pg.time.Clock()

#saving mobs as rectangles in mobs_rect and the mobs object in mobs
def mobs_create():
    mobs=[]
    mobs_rect=[]
    enemy = pg.image.load("enemy sprite slurp.png")

    for i in np.arange(5):
        mobs.append(Enemies(enemy, np.random.randint(-10,10), np.random.randint(-10,10),0,0))
        mobs_rect.append(mobs[i].pos)


    return np.array([mobs,mobs_rect])




def main():
    pg.init()
    GS = GameSettings()

    #getting the mobs objects from the function
    mobs = mobs_create()[0]

    #numpy array for the projectiles
    projectiles = np.zeros((100,2))

    #counter for the allocation of the projectiles into the array
    event_number = -1

    pg.display.init()
    screen = pg.display.set_mode((1920,1080),flags = pg.HWSURFACE|pg.FULLSCREEN)

    
    player = pg.image.load("Spielfigur.png").convert()
    background = pg.image.load("background.png").convert()
    projectile = pg.image.load("red_square.png").convert()
    
    running = True
    pg.mouse.set_visible(True)
    
    #getting the Player object
    #Player_0 = Player(player, 5, screen, background) 
    Player1 = Player(screen, pg.image.load("Spielfigur.png").convert(), (500,500),(0,0))

    while running:
        
        for event in pg.event.get():
            
            if  event.type == pg.KEYDOWN:
                
                if event.key == pg.K_SPACE:
                    #updating the counter
                    event_number += 1
                    #assining the projectiles coordinates [x,y,length,height] to the array
                    #the index is given by the event_number counter
                    projectiles[event_number] = (Player1.pos)
                if event.key == pg.K_ESCAPE:
                    running = False

       
        screen.blit(background, (0,0))
        #adding (-5) to the y-Coordinate the projectiles to "move" them 
        projectiles -= np.array([0,5])
        for m in np.arange(event_number+1):
            #only consider the projectiles which are not zero at the x-coordinate to
            #prevent the zeros to get blitted
            if projectiles[m,0] > 0:
                screen.blit(projectile, (projectiles[m,0], projectiles[m,1]))

            #delete the projectiles which are actually projectiles (x > 0) and are out of the screen (y < 0)
            if projectiles[m,1] < 0 and projectiles[m,0] > 0:
                projectiles[m]=np.zeros((2))
            
            #reset the timer when more than 70 projectiles were in game 
            if m == 70:
                event_number = 0
     
       

        #blit the players position and the movement
        gf.check_events(Player1)
        Player1.checkKeys()
        Player1.update()
        gf.update_screen(GS, background, Player1)
        
        #blit the mobs
        for m in mobs:   
            m.move()
            screen.blit(m.image,m.pos)
        
        pg.display.update()
        Clock.tick(120)


main()