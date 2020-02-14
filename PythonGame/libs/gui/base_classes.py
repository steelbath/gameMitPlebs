
from types import FunctionType as Function

import pygame as pg

from .fonts import Font
from ..utility.classes import Position, Color
from ..utility.input import Input


class GUI_STATIC(object):
    """Holds static global information for GUI"""
    active_screen = None
    active_gui = None
    focused_element = None
    hovered_element = None
    listen_text_input = False

    @classmethod
    def set_focused_element(cls, element):
        if element == cls.focused_element:
            return

        if cls.focused_element:
            cls.focused_element.blur()
        cls.focused_element = element

    @classmethod
    def set_hovered_element(cls, element):
        if element == cls.hovered_element:
            return

        if cls.hovered_element:
            cls.hovered_element.exit()
        cls.hovered_element = element

    @classmethod
    def set_active_gui(cls, gui):
        cls.active_gui = gui
        cls.active_screen = gui.screen

    @classmethod
    def update(cls):
        cls.active_gui.update()


class Element(object):
    """Base class for GUI elements"""
    interactive = False

    def __init__(self, position: Position, shape: 'Shape', color: Color = None,
                 image_name: str = None):
        if not color and not image_name:
            raise AttributeError("You must give color or image_name when declaring %s"
                                 % self.__name__)

        self.position = position
        self.shape = shape
        self.shape.element = self

        if image_name:
            self.shape.set_image(self._load_image(image_name))
        else:
            self.shape.set_color(color)

    def draw(self):
        self.shape.draw()

    def get_center(self) -> Position:
        return self.position + Position(
            self.shape.get_width() / 2, self.shape.get_height() / 2
        )

    @property
    def as_rect(self):
        return self.position.as_tuple + (self.shape.get_width(), self.shape.get_height())

    def _load_image(self, name):
        return pg.image.load(name).convert()

    def check_hit(self, pos: Position):
        return False


class InteractiveElement(Element):
    """Base class for interactive GUI elements"""

    # Contains events what the GUI should ignore if this is focused
    internal_event_handling = set()

    def __init__(self, image_on_hover: str = None, image_on_press: str = None,
                 *args, **kwargs):
        self.active = True
        self.focused = False
        self.hovered = False
        if image_on_hover:
            self.image_on_hover = self._load_image(image_on_hover)
        if image_on_press:
            self.image_on_press = self._load_image(image_on_press)
        super().__init__(*args, **kwargs)

    def check_hit(self, pos: Position):
        hit = self.shape.check_hit(pos.normalize_to(self.position))
        if hit and not self.hovered:
            self.enter()
        return hit

    def enter(self):
        GUI_STATIC.set_hovered_element(self)
        self.hovered = True

    def exit(self):
        self.hovered = False
        if GUI_STATIC.hovered_element == self:
            GUI_STATIC.hovered_element = None

    def update(self):
        """Called, when pointer is on top of elements shape"""
        if Input.mouse_up(pg.BUTTON_LEFT):
            self.focused = True
            GUI_STATIC.set_focused_element(self)

    def blur(self):
        """Called, when focus is lost from this element"""
        self.focused = False
        if GUI_STATIC.focused_element == self:
            GUI_STATIC.focused_element = None


class InputElement(InteractiveElement):
    """Base class for GUI input elements"""
    def __init__(self, on_change: Function = None, *args, **kwargs):
        self.input = None
        super().__init__(*args, **kwargs)

    def _value_changed(self):
        raise NotImplementedError()

    def set_input(self, value):
        self.input = value
        self._value_changed()

    def get_input(self):
        return self.input
        

class Shape(object):
    def __init__(self):
        self.element = None
        self.image = None
        self._use_color_only = False

    def set_image(self, image):
        self.image = image

    def set_color(self, color):
        self.dark_color = color.clone().darken()
        self.light_color = color.clone().lighten()
        self.default_color = color.clone()
        self.color = color
        self._use_color_only = True

    def get_width(self):
        raise NotImplementedError("`get_width` is not implemented in %s" % self.__name__)

    def get_height(self):
        raise NotImplementedError("`get_height` is not implemented in %s" % self.__name__)

    def check_hit(self, normalized_pos: Position):
        """Checks that position normalized to center of shape is within
            boundaries of shape
        """
        raise NotImplementedError(
            "%s does not implement `check_hit` function" % self.__name__
        )

    def draw(self):
        raise NotImplementedError()
