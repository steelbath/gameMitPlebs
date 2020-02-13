
import pygame as pg
from pygame.time import Clock
from utility.classes import Position
from utility.timing import Timing


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

    # KEYBOARD_DOWN
    #region
    @classmethod
    def key_down(cls, *keys):
        return cls._keys_down.issuperset(keys)

    @classmethod
    def any_key_down(cls):
        return bool(cls._keys_down)

    @classmethod
    def one_of_keys_down(cls, *keys):
        for key in keys:
            if key in cls._keys_down:
                return True
        return False
    #endregion

    # KEYBOARD_HELD
    #region
    @classmethod
    def key_held(cls, *keys):
        return cls._keys_held.issuperset(keys)

    @classmethod
    def any_key_held(cls):
        return bool(cls._keys_down)

    @classmethod
    def one_of_keys_held(cls, *keys):
        for key in keys:
            if key in cls._keys_held:
                return True
        return False
    #endregion

    # KEYBOARD_PRESSED
    #region
    @classmethod
    def key_pressed(cls, *keys):
        # Check for held keys first, as it is most common case
        return cls._keys_held.issuperset(keys) or cls._keys_down.issuperset(keys)

    @classmethod
    def any_key_pressed(cls):
        # Check for held keys first, as it is most common case
        return bool(cls._keys_held) or bool(cls._keys_down)

    @classmethod
    def one_of_keys_pressed(cls, *keys):
        for key in keys:
            if key in cls._keys_held or key in cls._keys_down:
                return True
        return False
    #endregion

    # KEYBOARD_UP
    #region
    @classmethod
    def key_up(cls, *keys):
        return cls._keys_up.issuperset(keys)

    @classmethod
    def any_key_up(cls):
        return bool(cls._keys_up)

    @classmethod
    def one_of_keys_up(cls, *keys):
        for key in keys:
            if key in cls._keys_up:
                return True
        return False
    #endregion

    # MOUSE_DOWN
    #region
    @classmethod
    def mouse_down(cls, *buttons):
        return cls._mouse_down.issuperset(buttons)

    @classmethod
    def any_mouse_down(cls):
        return bool(cls._mouse_down)

    @classmethod
    def one_of_buttons_down(cls, *buttons):
        for button in buttons:
            if button in cls._mouse_down:
                return True
        return False
    #endregion

    # MOUSE_HELD
    #region
    @classmethod
    def mouse_held(cls, *buttons):
        return cls._mouse_held.issuperset(buttons)

    @classmethod
    def any_mouse_held(cls):
        return bool(cls._mouse_held)

    @classmethod
    def one_of_buttons_held(cls, *buttons):
        for button in buttons:
            if button in cls._mouse_held:
                return True
        return False
    #endregion

    # MOUSE_PRESSED
    #region
    @classmethod
    def mouse_pressed(cls, *buttons):
        # Check for held keys first, as it is most common case
        return cls._mouse_held.issuperset(buttons) or cls._mouse_down.issuperset(buttons)

    @classmethod
    def any_mouse_pressed(cls):
        # Check for held keys first, as it is most common case
        return bool(cls._mouse_held) or bool(cls._mouse_down)

    @classmethod
    def one_of_buttons_pessed(cls, *buttons):
        for button in buttons:
            if button in cls._mouse_held or button in cls._mouse_down:
                return True
        return False
    #endregion

    # MOUSE_UP
    #region
    @classmethod
    def mouse_up(cls, *buttons):
        return cls._mouse_up.issuperset(buttons)

    @classmethod
    def any_mouse_up(cls):
        return bool(cls._mouse_up)

    @classmethod
    def one_of_buttons_up(cls, *buttons):
        for button in buttons:
            if button in cls._mouse_up:
                return True
        return False
    #endregion
    
    @classmethod
    def _refresh_keys(cls):
        # Add keys which were down last frame to keys_held set, and remove keys that
        # are not held anymore
        cls._keys_held = cls._keys_held.union(cls._keys_down.difference(cls._keys_not_held))
        cls._keys_down = set()
        cls._keys_up = set()
        cls._keys_not_held = set()

        # Store user input, so we can use it for text input
        cls.user_input_down = pg.event.get(eventtype=pg.KEYDOWN)
        cls.user_input_up = pg.event.get(eventtype=pg.KEYUP)

        # Get keys down, also handle if it is being held
        for event in cls.user_input_down:
            cls._keys_down.add(event.key)

        # Get keys up, also handle if it is being held
        for event in cls.user_input_up:
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
    def refresh_input(cls, parse_input=False):
        # TODO/FIXME:
        # Process events, probably should be refactored somewhere,
        # where its only done once
        pg.event.pump()

        cls._refresh_keys()
        cls._refresh_mouse()

        if parse_input:
            InputText.parse_input()


class InputText(object):
    """Keeps track of user input when `parse_input` is called every frame.
    Relies heavily on Input class and its behavior.
    """
    _input_string = ""
    _initial_delay_passed = False
    _current_input_sent = False
    _last_input_time = 0
    initial_delay = 400
    repeat_delay = 33
    input_events = dict()

    @classmethod
    def _reset_delay(cls):
        cls._last_input_time = Timing.get_ticks()
        cls._initial_delay_passed = False
        cls._current_input_sent = False

    @classmethod
    def get_input(cls):
        # Cached input string for this frame, in case of multiple listeners
        if cls._input_string:
            return cls._input_string

        current_time = Timing.get_ticks()

        repeat_delay_passed = current_time > cls.repeat_delay + cls._last_input_time
        initial_delay_passed = current_time > cls.initial_delay + cls._last_input_time
        should_return_input = (
            cls._initial_delay_passed and repeat_delay_passed or
            not cls._initial_delay_passed and initial_delay_passed or
            not cls._current_input_sent
        )

        if should_return_input:
            # Set flags so that we can now repeat only, instead of other values
            if initial_delay_passed:
                cls._initial_delay_passed = True
            cls._current_input_sent = True
            cls._last_input_time = current_time

            # Get values from parsed events
            for value in cls.input_events.values():
                cls._input_string += value

            if cls.input_events and not cls._input_string:
                # Return true as a result to indicate that repeat was triggered for keys
                # that do not result in unicode, ie. backspace
                cls._input_string = True

        return cls._input_string

    @classmethod
    def parse_input(cls):
        # Clear input cache from this frame
        cls._input_string = ""

        # Store inputs which are found in `user_input_down` of Input
        if Input.user_input_down:
            # Clear input events so we dont spam old inputs, only ones last pressed
            input_events = dict()
            for event in Input.user_input_down:
                # Ignore unicode on keys with special return values
                if event.key in (pg.K_BACKSPACE, pg.K_ESCAPE, pg.K_RETURN):
                    event.unicode = ""
                cls.input_events[event.key] = event.unicode

            # Reset delay as we just got new input
            cls._reset_delay()

        # Remove inputs which are found in `user_input_up` of Input
        for event in Input.user_input_up:
            if event.key in cls.input_events:
                del cls.input_events[event.key]
