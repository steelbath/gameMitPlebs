import pygame as pg

Clock = pg.time.Clock()
def hure():
    
    pg.display.init()
    screen=pg.display.set_mode(size=(1920,1080),flags = pg.FULLSCREEN|pg.HWSURFACE)
    
    x=0.0
    y=0.0
    player=pg.image.load("Spielfigur.png").convert()
    player_rect = player.get_rect()
    screen.blit(player,(x,y))
    pg.display.update()
    
    

    running = True
    
    pg.mouse.set_visible(True)
    

    while running:
        pressed = pg.key.get_pressed()
        
        if pressed[pg.K_LEFT]:
            x-=3
            position_new=player_rect.move(x,y)
            screen.fill(color=(0,0,0))
            screen.blit(player,position_new)
            pg.display.update()
        if pressed[pg.K_RIGHT]:
            x+=3
            position_new=player_rect.move(x,y)
            screen.fill(color=(0,0,0))
            screen.blit(player,position_new)
            pg.display.update()
        if pressed[pg.K_UP]:
            y-=3
            position_new=player_rect.move(x,y)
            screen.fill(color=(0,0,0))
            screen.blit(player,position_new)
            pg.display.update()
        if pressed[pg.K_DOWN]:
            y+=3
            position_new=player_rect.move(x,y)
            
            screen.fill(color=(0,0,0))
            screen.blit(player,position_new)
            pg.display.update()
            
        for event in pg.event.get():
            
            if event.type == pg.KEYDOWN:
                
                if event.key == pg.K_ESCAPE:
                    running = False
        Clock.tick(120)
        
        
hure()    