import pygame as pg
import GameFunctions as gf
import numpy as np
class GameSettings():

    def __init__(self):
        #screen
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (50,50,50)

class Creature():
    def __init__(self, screen, image, startpos:list=[0,0],speed:list=[0.0]):
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
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)
        

class Player(Creature):
    #MaxWalkSpeed
    MWS=3.5
    ACCEL=0.15
    def __init__(self, *args):
        #up left down right
        self.direction = [0, 0]
        self.facing = [0,-1]
        super().__init__(*args)
        #projectile array and last bullet var
        self.projectiles = np.zeros((100,4),dtype=int)
        self.lb = 0
        self.shooting=0
        self.shoottickcount=0
        #tweakables
        self.shootspeed=10
        self.bulletspeed = 6

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
        #shoot if space pressed
        if self.shooting:
            if self.shoottickcount==0:
                self.shoot(self.facing,self.pos)
                self.shoottickcount=self.shootspeed
            else: self.shoottickcount-=1
        if self.direction[0]:self.facing[0]= self.direction[0]
        elif self.direction[1]:self.facing[0]=0
        if self.direction[1]:self.facing[1]= self.direction[1]
        elif self.direction[0]:self.facing[1]=0
   
    def shoot(self, sdirection, spos):
        i=self.lb
        self.projectiles[i,0] = spos[0] 
        self.projectiles[i,1] = spos[1] 
        self.projectiles[i,2] = sdirection[0]*self.bulletspeed
        self.projectiles[i,3] = sdirection[1]*self.bulletspeed
        if not self.lb<99:self.lb=0
        else: self.lb+=1
        

