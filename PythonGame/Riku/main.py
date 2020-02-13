
import pygame

from gui.layout.classes import Layout, LAYOUT_DIRECTION
from gui.base_classes import GUI_STATIC
from gui.classes import GUI, Button, Rect, Text, TextElement, TEXT_ALIGN
from gui.fonts import Font
from utility.classes import Color, Position
from utility.input import Input, InputText
from utility.timing import Timing


def main():
    pygame.init()
    pygame.display.set_caption("GUI testing")
    screen = pygame.display.set_mode((1080,920))
    screen.fill((0,0,0))
    
    # Main menu
    main_menu = GUI(screen)
    main_menu.set_background_color(Color.black)

    # Settings menu
    settings_menu = GUI(screen)
    settings_menu.set_background_color(Color.black)

    def clickered():
        print("clikety clakety")

    def open_settings():
        GUI_STATIC.set_active_gui(settings_menu)

    def open_menu():
        GUI_STATIC.set_active_gui(main_menu)

    text_options = {
        "horizontal_align": TEXT_ALIGN.CENTER,
        "vertical_align": TEXT_ALIGN.CENTER,
    }
    button_defaults = {
        "position": Position.zero,
        "color": Color.light_grey.lighten(),
        "text_options": text_options
    }

    # Setup main menu layout
    menu_buttons = [
        Button(text="Play", on_click=clickered, shape=Rect(80, 40), **button_defaults),
        Button(text="Options", on_click=open_settings, shape=Rect(80, 40), **button_defaults),
        Button(text="Credits", on_click=clickered, shape=Rect(80, 40), **button_defaults),
        Button(text="Exit game", on_click=clickered, shape=Rect(80, 40), **button_defaults),
    ]
    menu_layout = Layout(position=Position(50, 100), shape=Rect(80, 40), color=Color.dark_grey,
                         layout_direction=LAYOUT_DIRECTION.VERTICAL)
    for element in menu_buttons:
        menu_layout.add_element(element)
    main_menu.add_layout(menu_layout)
        
    # Setup settings layout
    setting_buttons = [
        Button(text="Game", on_click=clickered, shape=Rect(120, 40), **button_defaults),
        Button(text="Visual", on_click=clickered, shape=Rect(120, 40), **button_defaults),
        Button(text="Audio", on_click=clickered, shape=Rect(120, 40), **button_defaults),
        Button(text="Controls", on_click=clickered, shape=Rect(120, 40), **button_defaults),
        Button(text="Return", on_click=open_menu, shape=Rect(120, 40), **button_defaults),
    ]
    settings_layout = Layout(position=Position(100, 50), shape=Rect(80, 40), color=Color.dark_grey,
                             layout_direction=LAYOUT_DIRECTION.HORIZONTAL)
    for element in setting_buttons:
        settings_layout.add_element(element)
    settings_menu.add_layout(settings_layout)

    # Add text elements in both GUI's
    test_text = Text("Enter your thoughts here", Position(250, 220), Font(), Color.white)
    test_text_input = TextElement(
        position=Position(250, 250), shape=Rect(300, 40), font=Font,
        color=Color.light_grey.lighten(), text_options=text_options
    )
    GUI_STATIC.listen_text_input = True  # Supposed to only be on, when text input field is active
    
    main_menu.add_element(test_text_input)
    settings_menu.add_element(test_text_input)
    main_menu.add_element(test_text, drawn_only=True)
    settings_menu.add_element(test_text, drawn_only=True)

    GUI_STATIC.set_active_gui(main_menu)

    Timing.init()
    running = True
    while running:
        Input.refresh_input(GUI_STATIC.listen_text_input)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        GUI_STATIC.update()
        Timing.tick()

    print("Safely quit the progaram")


if __name__=="__main__":
    main()