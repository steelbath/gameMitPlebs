import pygame as pg
import numpy as np

Clock = pg.time.Clock()

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
class Player:
    
    def __init__(self, image, move_speed, screen, background):
        
        self.image = image
        self.move_speed = move_speed
        self.screen = screen
        self.background = background
        self.pos = image.get_rect().move(640, 360)
        
        

        self.x = 0
        self.y = 0

    def move(self, pressed, projectile, speed_x, speed_y):
        
        self.screen.blit(self.image, self.pos)
        self.pressed = pressed

        self.projectile = projectile
        self.projectile_pos = self.pos
        self.speed_x = speed_x
        self.speed_y = speed_y
        
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
        




def mobs_create():
    mobs=[]
    mobs_rect=[]

    enemy = pg.image.load("enemy sprite slurp.png")

    for i in np.arange(5):
        mobs.append(Enemies(enemy, np.random.randint(-10,10), np.random.randint(-10,10),0,0))
        mobs_rect.append(mobs[i].pos)


    return np.array([mobs,mobs_rect])




def main():
    mobs = mobs_create()[0]

    projectile_position = []
    projectile_position_1 = []

    pg.display.init()
    screen = pg.display.set_mode((1920,1080),flags = pg.HWSURFACE|pg.FULLSCREEN)

    
    player = pg.image.load("Spielfigur.png").convert()
    background = pg.image.load("background.png").convert()
    projectile = pg.image.load("red_square.png").convert()
    
    running = True
    pg.mouse.set_visible(True)
    
    Player_0 = Player(player, 5, screen, background) 
    

    while running:
        
        for k in np.arange(len(projectile_position)):
               
                projectile_position_1.append(projectile_position[k].move(0,-10))
                  screen.blit(projectile, projectile_position_1[k])
                pg.display.update()
                if projectile_position_1[k].top < 0:
         
                    del projectile_position_1[k]
        projectile_position = []
        projectile_position = projectile_position_1
        projectile_position_1 = []
        for m in mobs:
            screen.blit(background, (0,0))
        
        
        for event in pg.event.get():
          
            if  event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    
                    projectile_position.append(Player_0.move(pg.key.get_pressed(),projectile,10,10))
                    print(projectile_position)
                    proj_position = np.array(projectile_position)
                    print(proj_position.shape)
                if event.key == pg.K_ESCAPE:
                    running = False

        
        Player_0.move(pg.key.get_pressed(),projectile,10,10)
        
        
        for m in mobs:   
            m.move()
            screen.blit(m.image,m.pos)
        
        pg.display.update()
        Clock.tick(100)


main()