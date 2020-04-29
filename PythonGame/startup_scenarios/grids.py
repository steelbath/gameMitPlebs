
import pygame
import timeit
import numpy  as np 
from ctypes import *

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
    # Game.running = True  # Main game loop
    Game.state = GameState.RUNNING

    setup_c = """
from ctypes import CDLL, ARRAY, POINTER, c_bool, c_int
import numpy as np
radius = 800
diameter = radius * 2
dll = CDLL("dynamic_libs/AdvancedMathUtils.dll")
dll.map_circle.argtypes = (c_int, ARRAY(ARRAY(c_bool, diameter), diameter), )  # Set accepted arguments of the function
map_circle = dll.map_circle
    """

    c_func = """
arr = np.zeros([diameter, diameter], dtype=c_bool)
arr_ptr = np.ctypeslib.as_ctypes(arr)
ret_val = map_circle(radius, arr_ptr)
    """

    commented = """
    dll = CDLL("dynamic_libs/AdvancedMathUtils.dll")  # Load dynamic link library
    dll.map_circle.argtypes = (  # Set accepted arguments of the function
        c_int,
        ARRAY(ARRAY(c_bool, diameter), diameter),
    )  
    map_circle = dll.map_circle

    radius = 5
    diameter = radius * 2
    arr = np.zeros([diameter, diameter], dtype=c_bool)
    arr_ptr = np.ctypeslib.as_ctypes(arr)  # Get pointer to array
    map_circle(radius, arr_ptr)  # Call C function which populates pointed array

    # Now arr has circle
    print(arr)
    """

    print("C function", timeit.timeit(setup=setup_c, stmt=c_func, number=100))
    
    setup_python = """
import math
from libs.utility.classes import Position
    """
    
    setup_python_numpy = """
import numpy as np
import math
    """

    other_numpy = """
radius = 800
r = radius # radius
diameter = radius * 2
r_mag = r * r
ox = radius
oy = radius # origin
arr = np.zeros([diameter, diameter], dtype=bool)

for x in range(int(-radius), int(radius)):
    height = math.sqrt(r_mag - x * x)

    for y in range(int(-height), int(height)):
        arr[x + ox, y + oy] = True
    """
    print("Other numpy",
        timeit.timeit(setup=setup_python_numpy, stmt=other_numpy, number=1)
    )
    other = """
center = Position.zero
radius = 800.0
points = []
r = radius # radius
r_mag = r * r
ox = center.x
oy = center.y # origin

for x in range(int(-radius), int(radius)):
    height = math.sqrt(r_mag - x * x)

    for y in range(int(-height), int(height)):
        points.append((x + ox, y + oy))
    """
    print("Other",
        timeit.timeit(setup=setup_python, stmt=other, number=1)
    )

    my_func = """
center = Position.zero
radius = 800.0
points = []
done = set()
pi = 3.1415
half_circle = int(radius * pi)
radian_jump = pi / half_circle
iridus = int(radius)

for i in range(0, half_circle):
    radians = radian_jump * i
    ex = math.ceil(math.sin(radians) * radius)
    ey = math.ceil(math.cos(radians) * radius)

    y = ey + center.y
    if y not in done:
        done.add(y)
        for x in range(-ex, ex):
            points.append((x + center.x, y))
    """
    print("My func", timeit.timeit(setup=setup_python, stmt=my_func, number=1))

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

        circle = grid.get_blocks_in_circle(Input.mouse_pos, 120.0, relative=True)
        for point in circle:
            # grid.set_block(point, True) - Inlined for performance
            grid.blocks[point[0] + point[1] * grid.width].value = True

        grid.draw()
        # Refresh pygame display after drawing all GUI elements
        pygame.display.update()
        
        for point in circle:
            # grid.set_block(point, None) - Inlined for performance
            grid.blocks[point[0] + point[1] * grid.width].value = None

        # Tick frames forward
        print("FPS:", Timing.get_fps())
        Timing.tick()

    print("Safely quit the program")


if __name__=="__main__":
    main()
