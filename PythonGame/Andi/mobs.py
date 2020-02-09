import pygame as pg
import numpy as np

Clock = pg.time.Clock()
class Enemies:
    
    def __init__(self,image,speed_x,speed_y,x,y):
        self.x = x
        self.y = y
        self.image = image
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.pos = image.get_rect().move(self.x,self.y)
        

    def move(self):
        self.pos = self.pos.move(self.speed_x,self.speed_y)
        if self.pos.right > 1280:

            self.speed_x = np.random.randint(-10,-1)
        if self.pos.left < 0:
            self.speed_x = np.random.randint(1,10)
        if self.pos.top < 0:
            self.speed_y = np.random.randint(1,10)
        if self.pos.bottom > 720:
            self.speed_y = np.random.randint(-10,-1)
mobs=[]
mobs_rect=[]
enemy = pg.image.load("enemy sprite slurp.png")
a=np.array([0,640,1000])
b=np.array([0,360,500])

for i in range(10):
    mobs.append(Enemies(enemy,np.random.randint(-10,10),np.random.randint(-10,10),np.random.choice(a,1)[0],np.random.choice(b,1)[0]))
    mobs_rect.append(mobs[i].pos)
def hure():
    
    pg.display.init()
    screen=pg.display.set_mode(size=(1920,1080),flags= pg.HWSURFACE|pg.FULLSCREEN)
   
    player=pg.image.load("Spielfigur.png").convert()
    background=pg.image.load("background.png").convert()
    player_rect = player.get_rect()

    x = 640
    y = 360

    screen.blit(player,(x,y))
    pg.display.update()
    

    running = True
    
    pg.mouse.set_visible(True)
    

    while running:
        
        for m in mobs:
            screen.blit(background,(0,0))
            screen.blit(player,(x,y))
        pressed = pg.key.get_pressed()
        
        if pressed[pg.K_LEFT]:
            x-=5
            position_new=player_rect.move(x,y)
            screen.blit(background,(0,0))
            screen.blit(player,position_new)
            
        if pressed[pg.K_RIGHT]:
            x+=5
            position_new=player_rect.move(x,y)
            screen.blit(background,(0,0))
            screen.blit(player,position_new)
          
        if pressed[pg.K_UP]:
            y-=5
            position_new=player_rect.move(x,y)
            screen.blit(background,(0,0))
            screen.blit(player,position_new)
           
        if pressed[pg.K_DOWN]:
            y+=5
            position_new=player_rect.move(x,y)
            screen.blit(background,(0,0))
            screen.blit(player,position_new)
          
            
            
        for m in mobs:
            m.move()
            screen.blit(m.image,m.pos)
            #if pg.m.collidelist([m.pos]) != -1:
            #    continue
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

            
        pg.display.update()
        Clock.tick(200)
            
hure()
