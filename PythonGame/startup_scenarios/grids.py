
import pygame

from libs.gui.base_classes import GUI_STATIC
from libs.utility.classes import Color, Position
from libs.utility.input import Input, InputText
from libs.utility.timing import Timing
from libs.utility.grid import DebugGrid

from Riku.game_assets import Game, GameState, GameSettings


def main():
    pygame.init()
    pygame.display.set_caption("Grid testing")
    screen = pygame.display.set_mode(GameSettings.screen_size())
    screen.fill((0,0,0))

    GUI_STATIC.active_screen = screen
    
    grid = DebugGrid(
        Color.blue,
        width=256,
        height=256,
        pos=Position.zero,
        size=Position(*GameSettings.screen_size())
    )

    Timing.init()
    Timing.framerate = 60
    burnable_events = [pygame.ACTIVEEVENT, pygame.VIDEORESIZE, pygame.VIDEOEXPOSE, pygame.USEREVENT]
    Game.running = True  # Main game loop
    Game.state = GameState.RUNNING
    print("game start")
    while Game.running:
        # Process all the events
        pygame.event.pump()

        Input.refresh_input(GUI_STATIC.listen_text_input)

        if Game.state == GameState.RUNNING:
            screen.fill((0,0,0))  # Draw black backround for game
            
        # Some event burner loops, cant use event.get() as it kills input events
        for event_type in burnable_events:
            pygame.event.get(eventtype=event_type)

        for event in pygame.event.get(eventtype=pygame.QUIT):
            print("game quit")
            Game.running = False
            break

        circle = grid.get_blocks_in_circle(Input.mouse_pos, 60.0, relative=True)
        for point in circle:
            # grid.set_block(point, True) - Inlined for performance
            grid.blocks[point.x + point.y * grid.width].value = True

        grid.draw()
        # Refresh pygame display after drawing all GUI elements
        pygame.display.update()
        
        for point in circle:
            # grid.set_block(point, None) - Inlined for performance
            grid.blocks[point.x + point.y * grid.width].value = None

        # Tick frames forward
        print("FPS:", Timing.get_fps())
        Timing.tick()

    print("Safely quit the program")


if __name__=="__main__":
    main()
