import pygame as pg

Clock = pg.time.Clock()
def hure():
    
    pg.display.init()
    screen=pg.display.set_mode(size=(1920,1080),flags = pg.FULLSCREEN|pg.HWSURFACE)
    
    x=0.0
    y=0.0
    player=pg.image.load("Spielfigur.png").convert()
    background=pg.image.load("background.png").convert()
    player_rect = player.get_rect()
    screen.blit(background,(0,0))
    screen.blit(player,(x,y))
    pg.display.update()

    running = True
    
    pg.mouse.set_visible(True)
    

    while running:
        pressed = pg.key.get_pressed()
        
        if pressed[pg.K_LEFT]:
            x-=3
            position_new=player_rect.move(x,y)
            screen.blit(background,(0,0))
            screen.blit(player,position_new)
            pg.display.update()
        if pressed[pg.K_RIGHT]:
            x+=3
            position_new=player_rect.move(x,y)
            screen.blit(background,(0,0))
            screen.blit(player,position_new)
            pg.display.update()
        if pressed[pg.K_UP]:
            y-=3
            position_new=player_rect.move(x,y)
            screen.blit(background,(0,0))
            screen.blit(player,position_new)
            pg.display.update()
        if pressed[pg.K_DOWN]:
            y+=3
            position_new=player_rect.move(x,y)
            screen.blit(background,(0,0))
            screen.blit(player,position_new)
            pg.display.update()
            
        for event in pg.event.get():
            
            if event.type == pg.KEYDOWN:
                
                if event.key == pg.K_ESCAPE:
                    running = False
        Clock.tick(120)
        
        
hure()    

class Enemies:
    def _init_(self,image,speed_x,speed_y):
        self.image = image
        self.speed_x = speed_x
        self.speed_y =speed_y
        self.pos = image.get.rect().move()


    def move(self):
        self.pos = self.pos.move(speed_x,speed_y)
        if self.pos.right > 1080:
            self.speed_x = -speed_x
        if self.pos.left < 0:
            self.speed_x = -speed_x
        if self.pos.top < 0:
            self.speed_y = -speed_y
        if self.pos.bottom > 1920:
            self.speed_y = -speed_y

