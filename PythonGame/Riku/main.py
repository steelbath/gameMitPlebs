
import pygame

from gui.base_classes import GUI_STATIC
from gui.classes import GUI, Button, Rect, Text
from utility.classes import Color, Position
from utility.input import Input, TextInput
from utility.timing import Timing


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
    GUI_STATIC.set_active_gui(gui_manager)
    GUI_STATIC.listen_text_input = True  # Supposed to only be on, when text input field is active

    Timing.init()
    running = True
    received_input = ""
    while running:
        Input.refresh_input(GUI_STATIC.listen_text_input)
        received_input += TextInput.get_input()
        print(received_input)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        GUI_STATIC.update()
        Timing.tick()

    print("Safely quit the progaram")


if __name__=="__main__":
    main()