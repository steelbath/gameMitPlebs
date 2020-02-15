
import pygame
from pygame.time import Clock

from libs.gui.classes import GUI, Button, Rect, Text
from libs.utility.classes import Color, Position
from libs.utility.input import Input


def openMenu():
    menu=True
    while menu:
        menu_manager.update

    text_options = {
        "horizontal_align": Text.ALIGN_CENTER,
        "vertical_align": Text.ALIGN_CENTER,
    }
    menu_button1 = Button(
        text="continue", on_click=clickered, position=Position(480, 80),
        shape=Rect(120, 40), color=Color.light_grey.lighten(), text_options=text_options
    )
    menu_button2= Button(
        text="options", on_click=clickered, position=Position(480, 280),
        shape=Rect(120, 40), color=Color.light_grey.lighten(), text_options=text_options
    )
    menu_button3 = Button(
        text="quit", on_click=clickered, position=Position(480, 480),
        shape=Rect(120, 40), color=Color.light_grey.lighten(), text_options=text_options
    )           
    if Input.key_down(pygame.K_ESCAPE):
        menu=False

def main():
    pygame.init()
    pygame.display.set_caption("GUI testing")
    screen = pygame.display.set_mode((1080,920))
    screen.fill((0,0,0))

    gui_manager = GUI(screen)
    menu_manager = GUI(screen)
    menu_manager.set_background_color(Color.black)
    def clickered():
        print("Clicked!")

    text_options = {
        "horizontal_align": Text.ALIGN_CENTER,
        "vertical_align": Text.ALIGN_CENTER,
    }
    test_button = Button(
        text="test", on_click=clickered, position=Position(80, 80),
        shape=Rect(80, 40), color=Color.light_grey.lighten(), text_options=text_options
    )

    gui_manager.add_element(test_button) 
    
    cpos=500

    running = True
    clock = Clock()
    while running:
        # DEBUG: Set low framerate for debugging
        clock.tick_busy_loop(5)
        Input._refresh_keys()
        cpos-=1
        if cpos <= 0: cpos=500
        if Input.key_down(pygame.K_ESCAPE):
            openMenu()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
#        gui_manager.update()
        screen.fill((30,103,203))        
        pygame.draw.circle(screen,(255,255,255), [cpos,255],30)
        pygame.display.update()
    print("Safely quit the progaram")


if __name__=="__main__":
    main()