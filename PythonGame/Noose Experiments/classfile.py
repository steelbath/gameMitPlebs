import pygame as pg

class GameSettings():

    def __init__(self):
        #screen
        self.screen_width = 1024
        self.screen_height = 768
        self.bg_color = (50,50,50)

class Creature():
    def __init__(self, screen, image, startpos:tuple=(0,0),speed:tuple=(0.0)):
        self.screen = screen
        self.image = image
        self.rect = self.image.get_rect()
        #position and movement
        self.pos=list(startpos)
        self.speed = list(speed)
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
            elif self.rect.centerx <0:
                self.rect.centerx = 1024
            elif self.rect.centery > 768:
                self.rect.centery = 0
            elif self.rect.centery < 0:
                self.rect.centery = 768
    
    def blitme(self):

        self.screen.blit(self.image, self.rect)
        

class Player(Creature):
    pass

