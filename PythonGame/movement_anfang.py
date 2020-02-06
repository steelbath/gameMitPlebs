import pygame as pg


def main():
    
    pg.display.init()
    screen=pg.display.set_mode(size=(1920,1080),flags = pg.HWSURFACE|pg.FULLSCREEN)
    
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
     
        pg.event.pump()
        #pg.mouse.get_rel()
        
        
        
        for event in pg.event.get():
            
          
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    x-=5
                    position_new=player_rect.move(x,y)
                if event.key == pg.K_RIGHT:
                    x+=5
                    position_new=player_rect.move(x,y)
                if event.key == pg.K_UP:
                    y-=5
                    position_new=player_rect.move(x,y)
                if event.key == pg.K_DOWN:
                    y+=5
                    position_new=player_rect.move(x,y)
                if event.key == pg.K_ESCAPE:
                    running = False
                screen.fill(color=(0,0,0))
                screen.blit(player,position_new)
                pg.display.flip()
                


                
    

if __name__=="__main__":
    # call the main function
    main()