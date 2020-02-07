import pygame as pg
import numpy as np
class Enemies:
    def __init__(self,image,speed_x,speed_y):
        self.image = image
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.pos = image.get_rect().move(0,0)

    def move(self):
        self.pos = self.pos.move(self.speed_x,self.speed_y)
        if self.pos.right > 800:

            self.speed_x = np.random.randint(-10,-1)
        if self.pos.left < 0:
            self.speed_x = np.random.randint(1,10)
        if self.pos.top < 0:
            self.speed_y = np.random.randint(-10,-1)
        if self.pos.bottom > 800:
            self.speed_y = np.random.randint(1,10)
mobs=[]
enemy = pg.image.load("noose_fotze.png")


for i in range(10):
    mobs.append(Enemies(enemy,np.random.randint(-10,10),np.random.randint(-10,10)))
def hure():
    
    pg.display.init()
    screen=pg.display.set_mode(size=(1920,1080),flags= pg.HWSURFACE|pg.FULLSCREEN)
    
    
    x=0
    y=0
    player=pg.image.load("Spielfigur.png").convert()
    background=pg.image.load("background.png").convert()
    player_rect = player.get_rect()
    screen.blit(player,(x,y))
    pg.display.update()
    

    running = True
    
    pg.mouse.set_visible(True)
    

    while running:
        for m in mobs:
            screen.blit(background,(0,0))
            
        for m in mobs:
            m.move()
            screen.blit(m.image,m.pos)
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False
            
        pg.display.update()
        pg.time.delay(100)
            
hure()
