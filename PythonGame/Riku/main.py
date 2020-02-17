
import pygame

from libs.gui.layout.classes import Layout, LAYOUT_DIRECTION, LAYOUT_ALIGN
from libs.gui.base_classes import GUI_STATIC
from libs.gui.classes import GUI, Button, Rect, Text, TextElement, TEXT_ALIGN
from libs.gui.fonts import Font
from libs.utility.classes import Color, Position
from libs.utility.input import Input, InputText
from libs.utility.timing import Timing

from Riku.game_assets import Game, GameState, GameSettings
from Riku.player import Player


def main():
    pygame.init()
    pygame.display.set_caption("GUI testing")
    screen = pygame.display.set_mode(GameSettings.screen_size())
    screen.fill((0,0,0))
    
    # Main menu
    main_menu = GUI(screen)
    main_menu.set_background_color(Color.black)

    # Settings menu
    settings_menu = GUI(screen)
    settings_menu.set_background_color(Color.black)

    game_hud = GUI(screen)

    def clickered():
        print("clikety clakety")

    def start_game():
        Game.state = GameState.RUNNING
        GUI_STATIC.set_active_gui(game_hud)

        if Game.player is None:
            Game.player = Player(
                GUI_STATIC.active_screen,
                pygame.image.load("Spielfigur.png").convert(),
                (500,500),(0,0)
            )

    def back_to_menu():
        Game.state = GameState.MAIN_MENU
        GUI_STATIC.set_active_gui(main_menu)
        Game.player = None

    def open_settings():
        GUI_STATIC.set_active_gui(settings_menu)

    def open_menu():
        GUI_STATIC.set_active_gui(main_menu)

    def exit_program():
        Game.running = False

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
        Button(text="Play", on_click=start_game, shape=Rect(80, 40), **button_defaults),
        Button(text="Options", on_click=open_settings, shape=Rect(80, 40), **button_defaults),
        Button(text="Credits", on_click=clickered, shape=Rect(160, 40), **button_defaults),
        Button(text="Exit game", on_click=exit_program, shape=Rect(80, 40), **button_defaults),
    ]
    menu_layout = Layout(position=Position(50, 100), shape=Rect(100, 255), color=Color.dark_grey,
                         padding=5, spacing=20, layout_direction=LAYOUT_DIRECTION.VERTICAL,
                         layout_align=LAYOUT_ALIGN.CENTER)
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
    settings_layout = Layout(position=Position(100, 50), shape=Rect(660, 60), color=Color.dark_grey,
                             padding=5, spacing=5, layout_direction=LAYOUT_DIRECTION.HORIZONTAL)
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

    back_to_menu_btn = Button(text="Quit", on_click=back_to_menu, shape=Rect(120, 40), **button_defaults)
    game_hud.add_element(back_to_menu_btn)

    GUI_STATIC.set_active_gui(main_menu)
    Timing.init()
    burnable_events = [pygame.ACTIVEEVENT, pygame.VIDEORESIZE, pygame.VIDEOEXPOSE, pygame.USEREVENT]
    Game.running = True  # Main game loop
    while Game.running:
        # Process all the events
        pygame.event.pump()

        Input.refresh_input(GUI_STATIC.listen_text_input)

        if Game.state == GameState.RUNNING:
            screen.fill((0,0,0))  # Draw black backround for game
            print("\nFRAME :", Timing.frames_since_start)
            Game.player.update()
            Game.player.draw()
            
        # Some event burner loops, cant use event.get() as it kills input events
        for event_type in burnable_events:
            for event in pygame.event.get(eventtype=event_type):
                break

        for event in pygame.event.get(eventtype=pygame.QUIT):
            running = False
            break

        GUI_STATIC.update()

        # Refresh pygame display after drawing all GUI elements
        pygame.display.update()

        # Tick frames forward
        Timing.tick()

    print("Safely quit the program")


if __name__=="__main__":
    main()
