import numpy as np
import pygame as pg

class Enemy:
    def __init__(self, image, speed:list=[0,0], start_pos:list=[0,0]):
        self.image = image
        self.rect = self.image.get_rect()
        self.pos = np.array(list(start_pos))
        self.speed = np.array(list(speed))
        self.rect.centerx = start_pos[0]
        self.rect.centery = start_pos[1]
        self.collision = False
    def spieler_zerlegen(self):
        
        


        if self.collision == False:

            self.pos[0]+=self.speed[0]
            self.pos[1]+=self.speed[1]
            self.rect.centerx = int(self.pos[0])
            self.rect.centery = int(self.pos[1])
            if self.rect.centerx > 1280:
                self.speed[0] = np.random.random_sample()*(-10)
            if self.rect.centerx < 0:
                self.speed[0] = np.random.random_sample()*10
            if self.rect.centery < 0:
                self.speed[1] = np.random.random_sample()*10
            if self.rect.centery > 720:
                self.speed[1] = np.random.random_sample()*(-10)
            return self.rect
        


