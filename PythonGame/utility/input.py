
import pygame as pg
from utility.classes import Position


class Input(object):
    keys_down = set()
    keys_held = set()
    keys_up = set()
    keys_not_held = set()

    mouse_btn_down = set()
    mouse_btn_held = set()
    mouse_btn_up = set()
    mouse_btn_not_held = set()
    mouse_pos = Position.zero

    @classmethod
    def key_down(cls, key):
        return key in cls.key_down

    @classmethod
    def key_held(cls, key):
        return key in cls.key_held

    @classmethod
    def key_up(cls, key):
        return key in cls.key_up

    @classmethod
    def mouse_down(cls, button):
        return button in cls.mouse_btn_down

    @classmethod
    def mouse_held(cls, button):
        return button in cls.mouse_btn_held

    @classmethod
    def mouse_up(cls, button):
        return button in cls.mouse_btn_up
    
    @classmethod
    def _refresh_keys(cls):
        cls.keys_held = cls.keys_held.union(cls.keys_down.difference(cls.keys_not_held))
        cls.keys_down = set()
        cls.keys_up = set()
        cls.keys_not_held = set()

        # Get keys down, also handle if it is being held
        for event in pg.event.get(eventtype=pg.KEYDOWN):
            if event.key in cls.keys_down:
                cls.keys_held.add(event.key)
            cls.keys_down.add(event.key)

        # Get keys up, also handle if it is being held
        for event in pg.event.get(eventtype=pg.KEYUP):
            if event.key in cls.keys_held:
                cls.keys_held.remove(event.key)
            if event.key in cls.keys_down:
                # Hack to make sure that keys dont get stuck on 'held' position
                cls.keys_not_held.add(event.key)
            cls.keys_up.add(event.key)

    @classmethod
    def _refresh_mouse(cls):
        cls.mouse_btn_held = cls.mouse_btn_held.union(
            cls.mouse_btn_down.difference(cls.mouse_btn_not_held)
        )
        cls.mouse_btn_down = set()
        cls.mouse_btn_up = set()
        cls.mouse_btn_not_held = set()
        cls.mouse_pos = Position(*pg.mouse.get_pos())

        # Get mouse down, also handle if it is being held
        for event in pg.event.get(eventtype=pg.MOUSEBUTTONDOWN):
            if event.button in cls.mouse_btn_down:
                cls.mouse_btn_held.add(event.button)
            cls.mouse_btn_down.add(event.button)

        # Get mouse up, also handle if it is being held
        for event in pg.event.get(eventtype=pg.MOUSEBUTTONUP):
            if event.button in cls.mouse_btn_held:
                cls.mouse_btn_held.remove(event.button)
            if event.button in cls.mouse_btn_down:
                # Hack to make sure that mouse dont get stuck on 'held' position
                cls.mouse_btn_not_held.add(event.button)
            cls.mouse_btn_up.add(event.button)
            
    @classmethod
    def refresh_input(cls):
        # TODO/FIXME:
        # Process events, probably should be refactored somewhere,
        # where its only done once
        pg.event.pump()

        cls._refresh_keys()
        cls._refresh_mouse()
