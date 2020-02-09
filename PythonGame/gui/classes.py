
import pygame as pg
from gui.base_classes import *


class GUI(object):
    """Manager class for GUI elements"""
    _elements = list()  # List of all gui elements on screen

    # List of layouts containing their own elements, needed for 
    # tracking element order when changing selected interactive GUI element
    # via arrows or tab
    _layouts = list()  

    def __init__(self, screen):
        GUI_STATIC.active_screen = screen
        self.background_image = None
        self.background_color = None

    def update(self):
        # Draw background first
        if self.background_image:
            GUI_STATIC.active_screen.blit(self.background_image)
        elif self.background_color:
            GUI_STATIC.active_screen.fill(self.background_color.as_tuple)
        else:
            # Default to black background if None was set before
            self.background_color = Color.black
            GUI_STATIC.active_screen.fill(self.background_color.as_tuple)

        # TODO: Handle input here perhaps?

        # Then draw all the elements
        for elem in self._elements:
            elem.draw()

        # Refresh pygame display after drawing all GUI elements
        pg.display.update()

    def add_element(self, element):
        self._elements.append(element)

    def add_layout(self, layout):
        self._layouts.append(layout)

    def set_background_color(self, color: Color):
        self.background_color = color

    def set_background_image(self, image_name: str):
        image = pg.image.load(image_name).convert()
        self.background_image = image
        

class Button(InteractiveElement):
    interactive = True

    def __init__(self, text: [Text, str], text_options: dict = None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if isinstance(text, str):
            options = text_options or dict()
            text = Text(text, kwargs.get("position"), Font(), container=self, **options)
        self.text = text

    def draw(self):
        super().draw()
        self.text.draw()
        

class Rect(Shape):
    def __init__(self, width: int, height: int, *args, **kwargs):
        self.width = width
        self.height = height
        super().__init__(*args, **kwargs)

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def check_hit(self, normalized_pos: Position):
        """Checks that position normalized to center of shape is within
            boundaries of this rectangle
        """
        x, y = normalized_pos.as_tuple
        horizontal_align = vertical_align = False

        if x > -self.width / 2 and x < self.width / 2:
            horizontal_align = True
        if y > -self.height / 2 and y < self.height / 2:
            vertical_align = True

        # Are both X and Y aligned within the boundaries of this rectangle
        return horizontal_align and vertical_align

    def draw(self):
        screen = GUI_STATIC.active_screen
        if self._use_color_only:
            screen.fill(self.color.as_tuple, self.element.as_rect)
        else:
            screen.blit(self.image, self.element.position.as_rect)


class Circle(Shape):
    def __init__(self, diameter: int, *args, **kwargs):
        self.diameter = diameter
        super().__init__(*args, **kwargs)

    def get_width(self):
        return self.diameter

    def get_height(self):
        return self.diameter
