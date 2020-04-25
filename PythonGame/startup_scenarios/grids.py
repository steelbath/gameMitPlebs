
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

    Timing.init()
    burnable_events = [pygame.ACTIVEEVENT, pygame.VIDEORESIZE, pygame.VIDEOEXPOSE, pygame.USEREVENT]
    Game.running = True  # Main game loop
    while Game.running:
        # Process all the events
        pygame.event.pump()

        Input.refresh_input(GUI_STATIC.listen_text_input)

        if Game.state == GameState.RUNNING:
            screen.fill((0,0,0))  # Draw black backround for game
            
        # Some event burner loops, cant use event.get() as it kills input events
        for event_type in burnable_events:
            for event in pygame.event.get(eventtype=event_type):
                break

        for event in pygame.event.get(eventtype=pygame.QUIT):
            running = False
            break

        # Refresh pygame display after drawing all GUI elements
        pygame.display.update()

        # Tick frames forward
        Timing.tick()

    print("Safely quit the program")


if __name__=="__main__":
    main()
