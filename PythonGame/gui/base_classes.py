
from types import FunctionType as Function

import pygame as pg

from gui.fonts import Font
from utility.classes import Position, Color


class GUI_STATIC(object):
    """Holds static global information for GUI"""
    active_screen = None


class Text(object):
    def __init__(self, text: str, position: Position, font: Font, color: Color = None):
        self.text = text
        self.position = position
        self.font = font
        self.color = color or Color.black
        self._image = None

    def _build_image(self):
        self._image = self.font.render(msg, True, self.color, None)

    def draw(self):
        if not self._image:
            self._build_image()

            self.screen.fill(self.button_color, self.rect)
        GUI.screen.blit(self._image, self.msg_image_rect)


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
        return self.position + Position(self.shape.width / 2, self.shape.height / 2)

    @property
    def as_rect(self):
        return self.position.as_tuple + (self.shape.get_width(), self.shape.get_height())

    def _load_image(self, name):
        return pg.image.load(name).convert()


class InteractiveElement(Element):
    """Base class for interactive GUI elements"""
    def __init__(self, on_click: Function, image_on_hover: str = None,
                 image_on_press: str = None, *args, **kwargs):
        self.on_click = on_click
        if image_on_hover:
            self.image_on_hover = self._load_image(image_on_hover)
        if image_on_press:
            self.image_on_press = self._load_image(image_on_press)
        super().__init__(*args, **kwargs)

        def click(self):
            self.on_click()


class InputElement(InteractiveElement):
    """Base class for GUI input elements"""
    def __init__(self, on_change: Function = None, *args, **kwargs):
        self.input = None
        super().__init__(*args, **kwargs)

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
