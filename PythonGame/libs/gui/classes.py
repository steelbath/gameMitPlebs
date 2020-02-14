
from types import FunctionType as Function

import pygame as pg
from .base_classes import *
from ..utility.input import Input, InputText
from ..utility.timing import Timing


class GUI(object):
    """Manager class for GUI elements"""
    _elements = list()  # List of all gui elements without layout
    _drawn_elements = list()  # List of all gui elements without layout

    # List of layouts containing their own elements, needed for 
    # tracking element order when changing selected interactive GUI element
    # via arrows or tab
    _layouts = list()

    def __init__(self, screen):
        self._elements = list()
        self._drawn_elements = list()
        self._layouts = list()
        self.screen = screen
        self.background_image = None
        self.background_color = None

    def _handle_input(self):
        pos = Input.mouse_pos

        if GUI_STATIC.focused_element:
            # Check if currently focused element should still be focused
            if GUI_STATIC.focused_element.check_hit(pos):
                return GUI_STATIC.focused_element.update()
            else:
                if Input.any_mouse_pressed():
                    # Remove focus
                    GUI_STATIC.focused_element.blur()
                else:
                    GUI_STATIC.focused_element.exit()

                    # Still keep updating as it remains focused
                    GUI_STATIC.focused_element.update()

        if GUI_STATIC.hovered_element:
            # Check if currently hovered element should still be hovered
            if not GUI_STATIC.hovered_element.check_hit(pos):
                GUI_STATIC.hovered_element.exit()

        for i in range(len(self._layouts) -1, -1, -1):
            # Layout does similar input handling for its elements as this
            if self._layouts[i].update():
                # Layout succesfully updated some menu item
                return 

        for i in range(len(self._elements) -1, -1, -1):
            # Global elements, not contained in layouts
            if self._elements[i].check_hit(pos):
                return self._elements[i].update()

    def update(self):
        # Get user input and pass it onto top-most element
        self._handle_input()

        # Draw background first
        if self.background_image:
            GUI_STATIC.active_screen.blit(self.background_image)
        elif self.background_color:
            GUI_STATIC.active_screen.fill(self.background_color.as_tuple)

        # Then draw all the elements
        for elem in self._drawn_elements:
            elem.draw()

        for elem in self._elements:
            elem.draw()

        # Then draw all the layouts
        for layout in self._layouts:
            layout.draw()

        # Refresh pygame display after drawing all GUI elements
        pg.display.update()

    def add_element(self, element, drawn_only=False):
        if drawn_only:
            self._drawn_elements.append(element)
        else:
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

    def __init__(self, text: ['Text', str], on_click: Function, text_options: dict = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.on_click = on_click

        if isinstance(text, str):
            options = text_options or dict()
            text = Text(text, kwargs.get("position"), Font(), container=self, **options)
        self.text = text

    def draw(self):
        super().draw()
        self.text.draw()

    def exit(self):
        super().exit()
        self.shape.color = self.shape.default_color

    def update(self):
        # Handle mouse down on this element
        # TODO: No use for it currently

        # Handle mouse held on this element
        if Input.any_mouse_held():
            if self.shape._use_color_only:
                self.shape.color = self.shape.dark_color
        else:
            if self.shape._use_color_only:
                self.shape.color = self.shape.light_color

        # Handle mouse up on this element
        if Input.mouse_up(pg.BUTTON_LEFT):
            self.on_click()

            if self.shape._use_color_only:
                self.shape.color = self.shape.default_color

    def blur(self):
        """Internally called, when pointer is not on top of element"""

        # TODO: Track only focused elements, and when pointer leaves them
        #       then only call the blur, not always if update is not ran

        # Set color back to default
        if self.shape._use_color_only:
            self.shape.color = self.shape.default_color


class TextElement(InputElement):
    """Input element for getting user keyboard inputs"""
    internal_event_handling = set([
        pg.K_HOME, pg.K_END, pg.K_LEFT, pg.K_RIGHT, pg.K_BACKSPACE, pg.K_DELETE
    ])

    def __init__(self, font, on_change: Function = None, hint_text: str = "",
                 text_options: dict = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._font_base = font()
        self.font = self._font_base.build_font()
        self.input = ""

        # Setup text objects
        text_options = text_options or {}
        text_options.update({
            "horizontal_align": TEXT_ALIGN.LEFT,
            "vertical_align": TEXT_ALIGN.CENTER
        })
        self.hint_text = None
        if hint_text:
            self.hint_text = Text(
                hint_text, kwargs.get("position"), self._font_base, container=self,
                **text_options
            )

        self.text = Text(
            "", kwargs.get("position"), self._font_base, container=self, **text_options
        )

        # Visible cursor info
        self.cursor_position = 0
        self.blink_timer = 500
        self._cursor_image = pg.Surface(
            (self._font_base.size / 20 + 1, self._font_base.size)
        )
        self._cursor_image.fill(Color.black.as_tuple)  # TODO: Get inverse color
        self._cursor_blinking = True
        self._last_blink = 0

    def _value_changed(self):
        # Rebuild text with font and set it as image for shape
        self.text.set_text(self.input)

    def _handle_input(self):
        input = InputText.get_input()
        if input:
            input_before = self.input
            if input is not True:
                # Add input if it's not only special keys
                self.input = (
                    self.input[:self.cursor_position] + input +
                    self.input[self.cursor_position:]
                )
                self.cursor_position += len(input)

            if Input.key_pressed(pg.K_HOME):
                self.cursor_position = 0
            if Input.key_pressed(pg.K_END):
                self.cursor_position = len(self.input)
            if Input.key_pressed(pg.K_LEFT):
                if Input.one_of_keys_pressed(pg.K_LCTRL, pg.K_RCTRL):
                    # TODO: Move over whole word
                    pass
                else:
                    self.cursor_position = max(self.cursor_position -1, 0)
            if Input.key_pressed(pg.K_RIGHT):
                if Input.one_of_keys_pressed(pg.K_LCTRL, pg.K_RCTRL):
                    # TODO: Move over whole word
                    pass
                else:
                    self.cursor_position = min(
                        self.cursor_position +1, len(self.input)
                    )
                    
            if Input.key_pressed(pg.K_BACKSPACE):
                # Remove letter before cursor position
                self.input = (
                    self.input[:max(self.cursor_position -1, 0)] +
                    self.input[self.cursor_position:]
                )
                self.cursor_position = max(self.cursor_position - 1, 0)
            if Input.key_pressed(pg.K_DELETE):
                # Remove letter after cursor position
                self.input = (
                    self.input[:self.cursor_position] +
                    self.input[min(self.cursor_position +1, len(self.input)):]
                )

            if input_before != self.input:
                self._value_changed()

            # Reset blinker when typing anything
            self._cursor_blinking = False
            self._last_blink = Timing.get_ticks()

    def update(self):
        super().update()

        if self.focused:
            GUI_STATIC.listen_text_input = True
            if Input.any_key_pressed():
                # Get text input from TextInput class and then manipulate it depending
                # on special key presses
                self._handle_input()

            # Check blink timer
            last_blink = Timing.get_ticks()
            if last_blink > self._last_blink + self.blink_timer:
                self._cursor_blinking = not self._cursor_blinking
                self._last_blink = last_blink

    def draw(self):
        super().draw()

        if not self.input and self.hint_text:
            # Draw hint_text image
            self.hint_text.draw()
        else:
            # Draw typed text
            self.text.draw()

            # Blink the cursor if timer is full
            if not self._cursor_blinking:
                cursor_x_pos = self.font.size(self.input[:self.cursor_position])[0]
                if self.cursor_position > 0:
                    cursor_x_pos -= self._cursor_image.get_width()
                GUI_STATIC.active_screen.blit(
                    self._cursor_image, (
                        cursor_x_pos + self.position.x,
                        self.text._image_rect.y
                    )
                )

    def blur(self):
        super().blur()
        self._cursor_blinking = True
        GUI_STATIC.listen_text_input = False


class TEXT_ALIGN:
    CENTER = 0
    LEFT = 1
    RIGHT = 2
    TOP = 1
    BOTTOM = 2
    NONE = 3


class Text(object):
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
            if self.horizontal_align == TEXT_ALIGN.LEFT:
                self._image_rect.x = rect[0]
            elif self.horizontal_align == TEXT_ALIGN.CENTER:
                self._image_rect.x = center.x - self._image_rect.width / 2
            elif self.horizontal_align == TEXT_ALIGN.RIGHT:
                self._image_rect.x = rect[0] + rect[2] - self._image_rect.width

            # Align Y
            if self.vertical_align == TEXT_ALIGN.TOP:
                self._image_rect.y = rect[1]
            elif self.vertical_align == TEXT_ALIGN.CENTER:
                self._image_rect.y = center.y - self._image_rect.height / 2
            elif self.vertical_align == TEXT_ALIGN.BOTTOM:
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
        """Checks that position normalized to corner of shape is within
            boundaries of this rectangle
        """
        x, y = normalized_pos.as_tuple

        if not x > 0 or not x < self.width:
            return False
        if not y > 0 or not y < self.height:
            return False

        # Both X and Y are aligned within the boundaries of this rectangle
        return True

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
