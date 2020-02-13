
from types import FunctionType as Function

import pygame as pg

from gui.fonts import Font
from utility.classes import Position, Color
from utility.input import Input


class GUI_STATIC(object):
    """Holds static global information for GUI"""
    active_screen = None
    active_gui = None
    focused_element = None
    listen_text_input = False

    @classmethod
    def set_focused_element(cls, element):
        if element == cls.focused_element:
            return

        if cls.focused_element:
            cls.focused_element.blur()
        cls.focused_element = element

    @classmethod
    def set_active_gui(cls, gui):
        cls.active_gui = gui
        cls.active_screen = gui.screen

    @classmethod
    def update(cls):
        cls.active_gui.update()


class Text(object):
    ALIGN_CENTER = 0
    ALIGN_LEFT = 1
    ALIGN_RIGHT = 2
    ALIGN_TOP = 1
    ALIGN_BOTTOM = 2
    ALIGN_NONE = 3

    def __init__(self, text: str, position: Position, font: Font, color: Color = None,
                 container: 'Element' = None, vertical_align: int = 1,
                 horizontal_align: int = 1):
        self.text = text
        self.position = position
        self._font_base = font
        self.color = color or Color.black
        self._image = None
        self.container = container
        self.vertical_align = vertical_align
        self.horizontal_align = horizontal_align

    def _align_text_to_container(self):
        self._image_rect = self._image.get_rect()

        # Initially put the text where the position is set
        self._image_rect.x = self.position.x
        self._image_rect.y = self.position.y

        if self.container:
            # Get container values
            rect = self.container.as_rect
            center = self.container.get_center()

            # Align X
            if self.horizontal_align == self.ALIGN_LEFT:
                self._image_rect.x = rect[0]
            elif self.horizontal_align == self.ALIGN_CENTER:
                self._image_rect.x = center.x - self._image_rect.width / 2
            elif self.horizontal_align == self.ALIGN_RIGHT:
                self._image_rect.x = rect[0] + rect[2] - self._image_rect.width

            # Align Y
            if self.vertical_align == self.ALIGN_TOP:
                self._image_rect.y = rect[1]
            elif self.vertical_align == self.ALIGN_CENTER:
                self._image_rect.y = center.y - self._image_rect.height / 2
            elif self.vertical_align == self.ALIGN_BOTTOM:
                self._image_rect.y = rect[1] + rect[3] - self._image_rect.height

    def _render_text(self):
        self._image = self.font.render(self.text, True, self.color.as_tuple, None)
        self._align_text_to_container()

    def _build_image(self):
        self.font = self._font_base.build_font()
        self._render_text()

    def set_text(self, text):
        self.text = text
        self._render_text()

    def draw(self):
        screen = GUI_STATIC.active_screen
        if not self._image:
            self._build_image()

        screen.blit(self._image, self._image_rect)


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

    def check_hit(self, pos: Position):
        return False


class InteractiveElement(Element):
    """Base class for interactive GUI elements"""
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
        return self.shape.check_hit(pos.normalize_to(self.position))

    def enter(self):
        self.hovered = True

    def exit(self):
        self.hovered = False

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
