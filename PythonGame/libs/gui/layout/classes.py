
from ..base_classes import Element
from ...utility.classes import Position
from ...utility.input import Input


class LAYOUT_DIRECTION:
    HORIZONTAL = 1
    VERTICAL = 2


class LAYOUT_ALIGN:
    LEFT = 1
    RIGHT = 2
    CENTER = 3
    TOP = 1
    BOTTOM = 2


class Layout(Element):
    """Layout manager class, helps with organizing elements and controlling
    keyboard movement across elements and other layouts"""
    _elements = list()
    _drawn_elements = list()

    # Should we support layouts within layouts?
    # _layouts

    def __init__(self, layout_direction: LAYOUT_DIRECTION, spacing: int = 20,
                 padding: int = 5, layout_align: LAYOUT_ALIGN = LAYOUT_ALIGN.LEFT,
                 static_size: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._elements = list()
        self._drawn_elements = list()
        self._static_size = static_size
        self._largest_elem_side = 0
        self.direction = layout_direction
        self.alignment = layout_align
        self.spacing = spacing
        self.padding = padding
        self.first_position = self.get_initial_position()
        self._last_position = self.padding  # Hold only distance from first to last element

    def get_initial_position(self):
        if self.direction == LAYOUT_DIRECTION.HORIZONTAL:
            initial_pos = self.position + Position(self.padding, self.shape.get_height() / 2)
        else:
            initial_pos = self.position + Position(self.shape.get_width() / 2, self.padding)

        return initial_pos

    def _calculate_element_alignment(self, side_length):
        # Get self side length
        if self.direction == LAYOUT_DIRECTION.HORIZONTAL:
            side = self.shape.get_height() - self.padding * 2
        else:
            side = self.shape.get_width() - self.padding * 2

        if self.alignment == LAYOUT_ALIGN.LEFT:
            return -side / 2
        elif self.alignment == LAYOUT_ALIGN.RIGHT:
            return side / 2 - side_length
        else:
            return -side_length / 2

    def get_next_position(self, element):
        if self._last_position == self.padding:
            move = self._last_position
        else:
            move = self._last_position + self.spacing

        if self.direction == LAYOUT_DIRECTION.HORIZONTAL:
            move += element.shape.get_width()
            elem_side = element.shape.get_height()

            if not self._static_size:
                size_changed = False
                if self._largest_elem_side < elem_side:
                    self._largest_elem_side = elem_side
                    size_changed = True

                # Set shape size to match current layout element sizes
                self.shape.set_width(move + self.padding * 2)
                self.shape.set_height(self._largest_elem_side + self.padding * 2)

                if size_changed:
                    self._recalculate_positions()

            aligned_side = self._calculate_element_alignment(elem_side)
            position = self.first_position + Position(
                move - element.shape.get_width(), aligned_side
            )
        else:
            move += element.shape.get_height()
            elem_side = element.shape.get_width()

            if not self._static_size:
                size_changed = False
                if self._largest_elem_side < elem_side:
                    self._largest_elem_side = elem_side
                    size_changed = True

                # Set shape size to match current layout element sizes
                self.shape.set_height(move + self.padding * 2)
                self.shape.set_width(self._largest_elem_side + self.padding * 2)

                if size_changed:
                    self._recalculate_positions()

            aligned_side = self._calculate_element_alignment(elem_side)
            position = self.first_position + Position(
                aligned_side, move -element.shape.get_height()
            )

        self._last_position = move
        return position

    def _recalculate_positions(self):
        # Reset position args
        self.first_position = self.get_initial_position()
        self._last_position = self.padding

        # Recalculate
        for element in self._elements:
            element.position = self.get_next_position(element)

    def add_element(self, element, drawn_only=False):
        element.position = self.get_next_position(element)

        if drawn_only:
            self._drawn_elements.append(element)
        else:
            self._elements.append(element)

    def update(self):
        # Update elements in layout for user actions
        pos = Input.mouse_pos

        for i in range(len(self._elements) -1, -1, -1):
            if self._elements[i].check_hit(pos):
                self._elements[i].update()
                return True

    def draw(self):
        super().draw()

        # Draw all elements in layout
        for elem in self._drawn_elements:
            elem.draw()

        for elem in self._elements:
            elem.draw()


class DynamicLayout(Layout):
    # TODO: Resizes depending on amount and size of elements
    pass


class GridLayout(Layout):
    # TODO
    pass


class ScrollableLayout(object):
    # TODO
    pass


class CarouselLayout(object):
    # TODO
    pass
