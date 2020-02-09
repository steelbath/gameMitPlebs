
import pygame as pg
from utility.classes import Position, Color

from types import FunctionType as Function


class Element(object):
    """Base class for GUI elements"""
    interactive = False

    def __init__(self, position: Position, color: Color = None, image_name: str = None):
        if not color and not image_name:
            raise AttributeError("You must give color or image_name when declaring %s"
                                 % self.__name__)
        self.image = self._load_image(image_name)

    def draw(self):
        self.image.blit()

    def _load_image(self, name):
        return pg.image.load(name).convert()


class InteractiveElement(Element):
    """Base class for interactive GUI elements"""
    def __init__(self, on_click: Function, image_on_hover: str = None,
                 image_on_press: str = None, *args, **kwargs):
        self.on_click = on_click
        self.image_on_hover = self._load_image(image_on_hover)
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


class Button(InteractiveElement):
    interactive = True

    def __init__(self, text: str, on_click: Function, *args, **kwargs):
        self.text = text
        self.on_click = text
        super().__init__(*args, **kwargs)
        

class Shape(object):
    def click_hit(self, x: int, y: int):
        """Test if x and y are inside this shape and return True or False"""
        raise NotImplementedError(
            "%s does not implement `click_hit` function" % self.__name__
        )


class Rectangle(Shape):
    def __init__(self, width: int, height: int, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Circle(Shape):
    def __init__(self, diameter: int, *args, **kwargs):
        super().__init__(*args, **kwargs)