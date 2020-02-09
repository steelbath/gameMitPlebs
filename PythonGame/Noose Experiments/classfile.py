import pygame as pg

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
    ACCEL=3.4
    def __init__(self, *args):
        #up left down right
        self.pressedkeys = [False]*4
        super().__init__(*args)
       
    def update(self):
        #key handlings
        if self.pressedkeys[0] == True:       
            if self.speed[1] > self.MWS*-1:
                self.speed[1] -= self.ACCEL
        elif self.speed[1] < 0:
            if self.speed[1] > self.ACCEL*-1:
                self.speed[1] = 0;
            else: self.speed[1] += self.ACCEL
        if self.pressedkeys[1] == True:       
            if self.speed[0] > self.MWS*-1:
                self.speed[0] -= self.ACCEL
        elif self.speed[0] < 0 :
            if self.speed[0] > self.ACCEL*-1:
                self.speed[0] = 0;
            else: self.speed[0] += self.ACCEL
        if self.pressedkeys[2] == True:       
            if self.speed[1] < self.MWS:
                self.speed[1] += self.ACCEL
        elif self.speed[1] > 0 :
            if self.speed[1] < self.ACCEL:
                self.speed[1] = 0;
            else: self.speed[1] -= self.ACCEL
        if self.pressedkeys[3] == True:       
            if self.speed[0] < self.MWS:
                self.speed[0] += self.ACCEL
        elif self.speed[0] > 0 :
            if self.speed[0] < self.ACCEL*-1:
                self.speed[0] = 0;
            else:self.speed[0] -= self.ACCEL

        #moving
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
            

   


