
import pygame as pg
from utility.classes import Position


class Input(object):
    _keys_down = set()
    _keys_held = set()
    _keys_up = set()
    _keys_not_held = set()

    _mouse_down = set()
    _mouse_held = set()
    _mouse_up = set()
    _mouse_not_held = set()

    mouse_pos = Position.zero
    user_input = list()

    @classmethod
    def key_down(cls, key):
        return key in cls._keys_down

    @classmethod
    def key_held(cls, key):
        return key in cls._keys_held

    @classmethod
    def key_up(cls, key):
        return key in cls._keys_up

    @classmethod
    def mouse_down(cls, button):
        return button in cls._mouse_down

    @classmethod
    def mouse_held(cls, button):
        return button in cls._mouse_held

    @classmethod
    def mouse_up(cls, button):
        return button in cls._mouse_up
    
    @classmethod
    def _refresh_keys(cls):
        cls._keys_held = cls._keys_held.union(cls._keys_down.difference(cls._keys_not_held))
        cls._keys_down = set()
        cls._keys_up = set()
        cls._keys_not_held = set()

        # Store user input, so we can use it for text input
        cls.user_input = pg.event.get(eventtype=pg.KEYDOWN)

        # Get keys down, also handle if it is being held
        for event in cls.user_input:
            if event.key in cls._keys_down:
                cls._keys_held.add(event.key)
            cls._keys_down.add(event.key)

        # Get keys up, also handle if it is being held
        for event in pg.event.get(eventtype=pg.KEYUP):
            if event.key in cls._keys_held:
                cls._keys_held.remove(event.key)
            if event.key in cls._keys_down:
                # Hack to make sure that keys dont get stuck on 'held' position
                cls._keys_not_held.add(event.key)
            cls._keys_up.add(event.key)

    @classmethod
    def _refresh_mouse(cls):
        cls._mouse_held = cls._mouse_held.union(
            cls._mouse_down.difference(cls._mouse_not_held)
        )
        cls._mouse_down = set()
        cls._mouse_up = set()
        cls._mouse_not_held = set()
        cls.mouse_pos = Position(*pg.mouse.get_pos())

        # Get mouse down, also handle if it is being held
        for event in pg.event.get(eventtype=pg.MOUSEBUTTONDOWN):
            if event.button in cls._mouse_down:
                cls._mouse_held.add(event.button)
            cls._mouse_down.add(event.button)

        # Get mouse up, also handle if it is being held
        for event in pg.event.get(eventtype=pg.MOUSEBUTTONUP):
            if event.button in cls._mouse_held:
                cls._mouse_held.remove(event.button)
            if event.button in cls._mouse_down:
                # Hack to make sure that mouse dont get stuck on 'held' position
                cls._mouse_not_held.add(event.button)
            cls._mouse_up.add(event.button)
            
    @classmethod
    def refresh_input(cls):
        # TODO/FIXME:
        # Process events, probably should be refactored somewhere,
        # where its only done once
        pg.event.pump()

        cls._refresh_keys()
        cls._refresh_mouse()
