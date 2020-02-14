
from ..base_classes import Element
from ...utility.classes import Position
from ...utility.input import Input


class LAYOUT_DIRECTION:
    HORIZONTAL = 1
    VERTICAL = 2


class Layout(Element):
    """Layout manager class, helps with organizing elements and controlling
    keyboard movement across elements and other layouts"""
    _elements = list()
    _drawn_elements = list()

    # Should we support layouts within layouts?
    # _layouts

    def __init__(self, layout_direction: LAYOUT_DIRECTION,spacing: int = 20,
                 padding: int = 5, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._elements = list()
        self._drawn_elements = list()
        self.direction = layout_direction
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

    def get_next_position(self, element):
        if self._last_position == self.padding:
            move = self._last_position
        else:
            move = self._last_position + self.spacing + self.padding

        if self.direction == LAYOUT_DIRECTION.HORIZONTAL:
            move += element.shape.get_width()
            position = self.first_position + Position(
                move - element.shape.get_width(), -element.shape.get_height() / 2
            )
        else:
            move += element.shape.get_height()
            position = self.first_position + Position(
                -element.shape.get_width() / 2, move -element.shape.get_height()
            )

        self._last_position = move
        return position

    def _recalculate_positions(self):
        # Reset position args
        self.first_position = self.get_initial_position()
        self._last_position = self.padding

        # Recalculate
        for element in self._elements:
            element.position = self.get_next_position()

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
