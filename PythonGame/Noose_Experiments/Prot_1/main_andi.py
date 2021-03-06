import numpy as np
import pygame as pg
import GameFunctions as gf
from andi_classes import *
import mobs_function as mobf

Clock = pg.time.Clock()

#saving mobs as rectangles in mobs_rect and the mobs object in mobs





def main():
    
    pg.display.init()
    screen = pg.display.set_mode((1920,1080),flags = pg.HWSURFACE|pg.FULLSCREEN)


    player = pg.image.load("Spielfigur.png").convert()
    background = pg.image.load("background.png").convert()
    projectile = pg.image.load("red_square.png").convert()
    
  
    running = True
    

    Player1 = Player(screen, pg.image.load("Spielfigur.png").convert(), (500,500))

    #create the Enemies using the Enemies.create() function in andi_classes
    mobs_list = mobf.mobs_function(2)[0]
    
    while running:

        screen.blit(background, (0,0))
        mobs_list = mobf.mobs_collision(2,mobs_list,screen)
        
        check_events_return = gf.check_events(Player1)
        projectiles, event_number, running = check_events_return[0], check_events_return[1], check_events_return[2]
        projectiles = Player1.shoot(projectile,projectiles)  
        if not pg.Rect(Player1.rect).collidelist(mobs_list) == -1:
            running = True
        #blit the players position and the movement
        
        Player1.checkKeys()
        Player1.update_2()
        screen.blit(player, Player1.pos)
        pg.display.update()
        Clock.tick(120)


main()