
import pygame

from gui.classes import GUI, Button, Rect, Text
from utility.classes import Color, Position


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
        "horizontal_align": Text.ALIGN_RIGHT,
        "vertical_align": Text.ALIGN_TOP,
    }
    test_button = Button(
        text="test", on_click=clickered, position=Position(80, 80),
        shape=Rect(80, 40), color=Color.white, text_options=text_options
    )

    gui_manager.add_element(test_button)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gui_manager.update()

    print("Safely quit the progaram")


if __name__=="__main__":
    main()