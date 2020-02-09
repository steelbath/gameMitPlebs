import pygame
import sys

class GameObject:
    def __init__(self, image , height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, height)
    def move(self):
        self.pos = self.pos.move(self.speed, 0)
        if self.pos.right > 600:
            self.pos.right = 0


def main():
    pygame.init()
    screen= pygame.display.set_mode((1024,768))
    player = pygame.image.load("Spielfigur.png").convert()
    background = pygame.image.load('background.png').convert()
    screen.blit(background, (0, 0))
    therect = pygame.draw.rect(screen, 250,(20, 500, 214, 43) )
    circlerect= pygame.draw.circle(screen, (145,132,123),(50,350),50)
    objects =[]
    print(therect)
    ob = GameObject (player, 200, 20)
    objects.append(ob)
    print(ob.image)

    while 1:
        for event in pygame.event.get():
            if event.type in (pygame.QUIT, pygame.KEYDOWN):
                sys.exit()
        for o in objects:
            screen.blit(background, o.pos, o.pos)
            if therect.x < 700:
               therect = therect.move(3,0)
               pygame.draw.rect(screen, 250,therect )
        for o in objects:
            o.move()
#            screen.blit(therect,)
            screen.blit(o.image, o.pos)
        pygame.display.update()
        pygame.time.delay(100)

main()
