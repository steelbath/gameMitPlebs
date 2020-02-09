import numpy as np
import pygame as pg


class Enemies:
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