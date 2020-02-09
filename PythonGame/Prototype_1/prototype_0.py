import pygame as pg
import numpy as np

Clock = pg.time.Clock()


import numpy as np
import pygame as pg





def mobs_create():
    mobs=[]
    mobs_rect=[]

    enemy = pg.image.load("enemy sprite slurp.png")

    for i in np.arange(5):
        mobs.append(Enemies(enemy, np.random.randint(-10,10), np.random.randint(-10,10),0,0))
        mobs_rect.append(mobs[i].pos)


    return np.array([mobs,mobs_rect])




def main():
    mobs = mobs_create()[0]

    projectiles = np.zeros((100,4))
    event_number = -1

    pg.display.init()
    screen = pg.display.set_mode((1920,1080),flags = pg.HWSURFACE|pg.FULLSCREEN)

    
    player = pg.image.load("Spielfigur.png").convert()
    background = pg.image.load("background.png").convert()
    projectile = pg.image.load("red_square.png").convert()
    
    running = True
    pg.mouse.set_visible(True)
    
    Player_0 = Player(player, 5, screen, background) 
    

    while running:
        
        

        for m in mobs:
            screen.blit(background, (0,0))

        projectiles -= np.array([0,5,0,0])
        for m in np.arange(event_number):
            if projectiles[m,0] > 0:
                screen.blit(projectile, (projectiles[m,0], projectiles[m,1]))
            if projectiles[m,1] < 0 and projectiles[m,0] > 0:
                projectiles[m]=np.zeros((4))
            if m == 60:
                event_number = 0
     
        
        


        for event in pg.event.get():
            
            if  event.type == pg.KEYDOWN:
                
                if event.key == pg.K_SPACE:
                    event_number += 1
                    projectiles[event_number] = (Player_0.move(pg.key.get_pressed(),projectile,10,10))
                    print(event_number)
                    print(projectiles)
                if event.key == pg.K_ESCAPE:
                    running = False

        
        Player_0.move(pg.key.get_pressed(),projectile,10,10)
        
        
        for m in mobs:   
            m.move()
            screen.blit(m.image,m.pos)
        
        pg.display.update()
        Clock.tick(100)


main()