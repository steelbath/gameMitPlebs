import numpy as np
import pygame as pg
import GameFunctions as gf


class Enemiez:
    def __init__(self, image, speed_x, speed_y, x, y):
        self.x = x
        self.y = y
        self.image = image
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.pos = image.get_rect().move(self.x, self.y)

    def move(self):
        self.pos = self.pos.move(self.speed_x, self.speed_y)
        if self.pos.right > 1280:
            self.speed_x = np.random.randint(-10,-1)
        if self.pos.left < 0:
            self.speed_x = np.random.randint(1,10)
        if self.pos.top < 0:
            self.speed_y = np.random.randint(1,10)
        if self.pos.bottom > 720:
            self. speed_y = np.random.randint(-10,-1)
class Playerz:
    
    def __init__(self, image, move_speed, screen, background):
        
        self.image = image
        self.move_speed = move_speed
        self.screen = screen
        self.background = background
        self.pos = image.get_rect().move(640, 360)
        
        

        self.x = 0
        self.y = 0
       

    def move(self, pressed):
        
        self.screen.blit(self.image, self.pos)
        self.pressed = pressed

        
        if self.pressed[pg.K_LEFT]:
    
            self.x = -self.move_speed
            self.pos = self.pos.move(self.x, self.y)
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.image, self.pos)
            self.x = 0
        
        if self.pressed[pg.K_RIGHT]:
            
            self.x = self.move_speed
            self.pos = self.pos.move(self.x, self.y)
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.image, self.pos)
            self.x = 0
        
        if self.pressed[pg.K_UP]:
            
            self.y = -self.move_speed
            self.pos = self.pos.move(self.x, self.y)
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.image, self.pos)
            self.y = 0
        
        if self.pressed[pg.K_DOWN]:
            
            self.y = self.move_speed
            self.pos = self.pos.move(self.x, self.y)
            self.screen.blit(self.background, (0,0))
            self.screen.blit(self.image, self.pos)
            self.y = 0
        return self.pos

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
           