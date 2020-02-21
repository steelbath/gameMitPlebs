import pygame as pg

#game settings to be exported into file 
class GS():
    screen_width=1024
    screen_height=768

class Game():
    done = False
    fps = 120
    screen =  pg.display.set_mode((GS.screen_width,GS.screen_height))
    Clock = pg.time.Clock()
    @classmethod
    def setup_states(cls, state_dict, start_state):
        cls.states = state_dict 
        cls.state_name = start_state
        cls.state = cls.states[cls.state_name]
    @classmethod
    def flip_state(cls):
        current_state = cls.state_name
        next_state = cls.state.next_state
        cls.state.done = False
        cls.state_name = next_state
        persistent = cls.state.persist
        cls.state = cls.states[cls.state_name]
        cls.state.startup(persistent)
    
    @classmethod
   

    def event_loop(self):
        #handle events
        pass


    while not cls.done:
        delta_time = cls.clock.tick(cls.fps)/1000.0
        cls.event_loop()
        cls.update(delta_time)
        pg.display.update()

class GameState(object):
    """
    Parent class for individual game states to inherit from. 
    """
    def __init__(self):
        cls.done = False
        cls.quit = False
        cls.next_state = None
        cls.screen_rect = pg.display.get_surface().get_rect()
        cls.persist = {}
        cls.font = pg.font.Font(None, 24)
        
    def startup(self, persistent):
        """
        Called when a state resumes being active.
        Allows information to be passed between states.
        
        persistent: a dict passed from state to state
        """
        cls.persist = persistent        
        
    def get_event(self, event):
        """
        Handle a single event passed by the Game object.
        """
        pass
        
    
    def update(self, dt):
        """
        Update the state. Called by the Game object once
        per frame. 
        
        dt: time since last frame
        """
        pass
        
    def draw(self, surface):
        """
        Draw everything to the screen.
        """
        pass



class GameMain(GameState):
