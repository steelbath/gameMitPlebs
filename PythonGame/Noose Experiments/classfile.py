import pygame as pg
import GameFunctions as gf

class GameObject():

    def __init__(self):
        #settings
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (50,50,50)
        #environmenntal objects

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

    def shoot(self, sdirection, spos):
            gf.projectiles[gf.pmap[0],0] = spos[0] 
            gf.projectiles[gf.pmap[0],1] = spos[1] 
            gf.projectiles[gf.pmap[0],2] = sdirection[0]*3
            gf.projectiles[gf.pmap[0],3] = sdirection[1]*3
            gf.pmap[0]+=1
            if gf.pmap[0] > 90:gf.pmap[0]=0



