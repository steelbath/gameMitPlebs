import numpy as np
import pygame as pg
import GameFunctions as gf


class Enemies:

    def __init__(self, image, speed:list=[0,0], start_pos:list=[0,0]):
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = np.array(list(start_pos))
        self.speed = np.array(list(speed))
        self.rect.centerx = start_pos[0]
        self.rect.centery = start_pos[1]
        self.topleft = pg.Rect(self.rect).topleft
        self.bottomright = pg.Rect(self.rect).bottomright

    def move(self):
        self.pos[0]+=self.speed[0]
        self.pos[1]+=self.speed[1]
        self.rect.centerx = int(self.pos[0])
        self.rect.centery = int(self.pos[1])
        self.topleft = pg.Rect(self.rect).topleft
        self.bottomright = pg.Rect(self.rect).bottomright
        
        if self.rect.left > 1024:
            self.speed[0] = np.random.random_sample()*(-10)
        if self.rect.right < 0:
            self.speed[0] = np.random.random_sample()*10
        if self.rect.top < 0:
            self.speed[1] = np.random.random_sample()*10
        if self.rect.bottom > 768:
            self.speed[1] = np.random.random_sample()*(-10)
        return self.rect
    


    def collision(self):
        self.speed[0] = -self.speed[0]
        self.speed[1] = -self.speed[1]
        

class GameSettings():

    def __init__(self):
        #screen
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (50,50,50)

class Creature():
    def __init__(self, screen, image, startpos:list=[0,0],speed:list=[0,0]):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        #position and movement
        self.pos=list(startpos)
        self.speed = list(speed)
        self.maxspeed = 2
        self.rect.centerx = startpos[0]
        self.rect.centery = startpos[1]
        
    def update(self):
        if self.speed != [0,0]:
            self.pos[0]+=self.speed[0]
            self.pos[1]+=self.speed[1]
            self.rect.centerx = int(self.pos[0])
            self.rect.centery = int(self.pos[1])
            if self.rect.centerx > 1024:
               self.rect.centerx = 0
               self.pos[0] = 0
            elif self.rect.centerx <0:
                self.rect.centerx = 1024
                self.pos[0] = 1024
            elif self.rect.centery > 768:
                self.rect.centery = 0
                self.pos[1] = 0
            elif self.rect.centery < 0:
                self.rect.centery = 768
                self.pos[1] = 768
    
    def shoot(self,projectile,projectiles):
        self.projectile = projectile
        self.projectiles = projectiles
        
        for m in np.arange(100):
            #only consider the projectiles which are not zero at the x-coordinate to
            #prevent the zeros to get blitted
            if self.projectiles[m,0] > 0:
                self.screen.blit(self.projectile, (self.projectiles[m,0], self.projectiles[m,1]))
            #delete the projectiles which are actually projectiles (x > 0) and are out of the screen (y < 0)
            if self.projectiles[m,1] < 0 and self.projectiles[m,0] > 0:
                self.projectiles[m]=np.zeros((2))
        self.projectiles -= np.array([0,5])
        return self.projectiles
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        

class Player(Creature):
    #MaxWalkSpeed
    MWS=3.5
    ACCEL=0.15
    def __init__(self, *args):
        #up left down right
        self.direction = [0, 0]
        self.projectiles = np.zeros((100,2))
        self.event_number = -1
        super().__init__(*args)
    def checkKeys(self):
# Check movement input
                
        # Apply drag and direction
        for i in [0,1]:
            if not self.direction[i] and self.speed[i]:
                # direction is zero but we still have speed
                if self.speed[i] < 0:
                    self.speed[i] += self.ACCEL
                    if self.speed[i] > 0:
                        self.speed[i] = 0
                else:
                    self.speed[i] -= self.ACCEL
                    if self.speed[i] < 0:
                        self.speed[i] = 0
            elif self.direction[i] and (abs(self.speed[i]) < self.MWS or not gf.csign(self.direction[i],self.speed[i])):
                #we have input and not max walk speed reached
                if gf.csign(self.direction[i],self.speed[i]):
                    self.speed[i] += self.ACCEL*self.direction[i]
                    if abs(self.speed[i])>self.MWS:self.speed[i]=self.MWS*self.direction[i]
                else:
                    self.speed[i] += 2*self.ACCEL*self.direction[i]    