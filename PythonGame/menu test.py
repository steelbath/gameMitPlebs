
import pygame
from pygame.time import Clock

from gui.classes import GUI, Button, Rect, Text
from utility.classes import Color, Position
from utility.input import Input


def main():
    pygame.init()
    pygame.display.set_caption("GUI testing")
    screen = pygame.display.set_mode((1080,920))
    screen.fill((0,0,0))

    gui_manager = GUI(screen)
    gui_manager.set_background_color(Color.black)

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
        print(Input.keys_down)
        cpos-=1
        if cpos <= 0: cpos=500
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