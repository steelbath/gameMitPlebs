
from pygame.time import Clock
from pygame import time
        

class Timing(object):
    framerate = 60
    frames_since_start = 0

    @classmethod
    def init(cls):
        cls.clock = Clock()

    @classmethod
    def get_time(cls):
        return cls.clock.get_time()

    @classmethod
    def get_fps(cls):
        return cls.clock.get_fps()

    @classmethod
    def tick(cls):
        cls.frames_since_start  += 1
        cls.clock.tick(cls.framerate)

    @staticmethod
    def get_ticks():
        return time.get_ticks()
