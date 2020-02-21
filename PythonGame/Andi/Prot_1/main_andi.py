import numpy as np
import pygame as pg
import GameFunctions as gf
from andi_classes import *
import module1 as modu

Clock = pg.time.Clock()


def main():
    number_of_mobs = 3
    pg.display.init()
    screen = pg.display.set_mode((1024,768))


    player = pg.image.load("Spielfigur.png").convert()
    background = pg.image.load("background.png").convert()
    projectile = pg.image.load("red_square.png").convert()
    
  
    running = True
    

    Player1 = Player(screen, pg.image.load("Spielfigur.png").convert(), (500,500))

    #create the Enemies using the Enemies.create() function in andi_classes
    mobs_list = modu.mobs_create(number_of_mobs)[1]
    mobs = modu.mobs_create(number_of_mobs)[0]
   
    while running:

        screen.fill((50,50,50))    
        mobs = modu.mobs_collide(number_of_mobs, mobs, mobs_list, screen)
        check_events_return = gf.check_events(Player1)
        projectiles, event_number, running = check_events_return[0], check_events_return[1], check_events_return[2]
        projectiles = Player1.shoot(projectile,projectiles)  
        if not pg.Rect(Player1.rect).collidelist(mobs_list) == -1:
            running = True
        #blit the players position and the movement
        print(mobs_list[1].left)
        #print(mobs_list[1].right)
        #print(mobs_list[1].top)
        #print(mobs_list[1].bottom)
        Player1.checkKeys()
        Player1.update()
        screen.blit(player, Player1.pos)
        pg.display.update()
        Clock.tick(120)


main()
