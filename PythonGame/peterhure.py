import pygame as pg
def hure():
    
    pg.display.init()
    screen=pg.display.set_mode(size=(800,600))
    
    x=0
    y=0
    player=pg.image.load("Spielfigur.png").convert()
    player_rect = player.get_rect()
    screen.blit(player,(x,y))
    pg.display.update()
    

    running = True
    
    pg.mouse.set_visible(True)
    pg.key.set_repeat(1,1)

    while running:
        pressed = pg.key.get_pressed()
        
        if pressed[pg.K_LEFT]:
            x-=1
            position_new=player_rect.move(x,y)
            screen.fill(color=(0,0,0))
            screen.blit(player,position_new)
            pg.display.flip()
        if pressed[pg.K_RIGHT]:
            x+=1
            position_new=player_rect.move(x,y)
            screen.fill(color=(0,0,0))
            screen.blit(player,position_new)
            pg.display.flip()
        if pressed[pg.K_UP]:
            y-=1
            position_new=player_rect.move(x,y)
            screen.fill(color=(0,0,0))
            screen.blit(player,position_new)
            pg.display.flip()
        if pressed[pg.K_DOWN]:
            y+=1
            position_new=player_rect.move(x,y)
            screen.fill(color=(0,0,0))
            screen.blit(player,position_new)
            pg.display.flip()
            
        
        
        for event in pg.event.get():
            
            if event.type == pg.KEYDOWN:
                
                if event.key == pg.K_ESCAPE:
                    running = False
        
        
hure()    


