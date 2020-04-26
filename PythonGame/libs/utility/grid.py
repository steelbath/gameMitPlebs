
import math

from libs.gui.base_classes import GUI_STATIC
from .classes import Position, Color


class Direction:
    """Enum for basic directions"""
    North = (0, -1)
    NorthWest = (1, -1)
    West = (1, 0)
    SouthWest = (1, 1)
    South = (0, 1)
    SouthEast = (-1, 1)
    East = (-1, 0)
    NorthEast = (-1, -1)


class Grid():
    _block_size: Position
    _pos: Position
    _size: Position  # Covered area
    width: int
    height: int
    blocks: list

    class OutOfBounds:
        pass

    def __init__(self, width, height, pos, size):
        self.width = width
        self.height = height
        self._pos = Position(pos.x, pos.y)
        self._size = Position(size.x, size.y)
        self.blocks = list()
        self._block_size = Position(
            size.x / width,
            size.y / height
        )

        for x in range(0, self.width * self.height):
            self.blocks.append(None)

    def relative_pos_to_grid(self, pos: Position) -> Position:
        if(pos.x < self._pos.x or pos.y < self._pos.y):
            return OutOfBounds  # The position cannot be on grid
        
        # Calibrate pos to grids start pos
        pos -= self._pos
        if(pos.x > self._size.x or pos.y > self._size.y):
            return OutOfBounds  # X or Y pos goes beyond the grid area

        grid_pos = Position(
            math.floor(pos.x / self._block_size.x),
            math.floor(pos.y / self._block_size.y)
        )
        return grid_pos

    def pos_is_on_grid(self, pos, relative=False) -> bool:
        if relative:
            pos = self.relative_pos_to_grid(pos)
            if pos is OutOfBounds:
                return False

        if pos.x < 0 or pos.y < 0:
            return False

        if pos.x > self.width or pos.y > self.height:
            return False
        return True

    def set_block(self, pos: Position, value):
        self.blocks[pos.x + pos.y * self.width] = value

    def get_block_at(self, pos: Position, relative=False) -> None:
        if relative:
            pos = self.relative_pos_to_grid(pos)
            if pos is OutOfBounds:
                return OutOfBounds

        return self.blocks[pos.x + pos.y * self.width]

    def get_block_towards(self, pos: Position, Direction: Direction, relative=False) -> None:
        if relative:
            pos = self.relative_pos_to_grid(pos)
            if pos is OutOfBounds:
                return OutOfBounds

        pos += Position(*Direction)
        return get_block_at(pos)

    def get_blocks_in_circle(self, pos: Position, radius: float, relative=False):
        if relative:
            pos = self.relative_pos_to_grid(pos)
        if not pos:
            return list()

        circle_pos = self._pos + pos
        circle = circle_pos.map_circle(radius)
        overlapping_points = list()
        for point in circle:
            if self.pos_is_on_grid(point):
                overlapping_points.append(point)

        return overlapping_points

    def get_blocks_in_square(self, pos: Position, size: Position, relative=False):
        if relative:
            pos = self.relative_pos_to_grid(pos)
        if not pos:
            return list()


class ZonedGrid(Grid):
    zone_width: int
    zone_height: int
    zones: list

    def __init__(self, zone_width, zone_height, *args, **kwargs):
        self.zone_width = zone_width
        self.zone_height = zone_height
        self.zones = list(zone_width * zone_height)

        def get_zones_at(self, x, y) -> list(Zone):
            pass

        def get_blocks_in_zones(self, zones) -> list:
            pass


class Zone(ZonedGrid):
    _grid: ZonedGrid
    surrounding_zones: list

    def __init__(self, grid, *args, **kwargs):
        self.grid = grid


class DebugGrid(Grid):
    def __init__(self, filled_color: Color, *args, empty_color=None, **kwargs):
        super().__init__(*args, **kwargs)

        self.blocks = list()
        for x in range(0, self.width * self.height):
            pos = Position(
                (1 + x % self.width) * self._block_size.x,
                math.floor(x / self.width) * self._block_size.y
            )
            self.blocks.append(DebugBlock(self._block_size, pos, filled_color, empty_color))

    def set_block(self, pos: Position, value):
        self.blocks[pos.x + pos.y * self.width].value = value
            
    def draw(self):
        # print(len(self.blocks))
        for block in self.blocks:
            # block.draw() - Inlined for performance

            if block.value:
                GUI_STATIC.active_screen.fill(
                    (block.filled_color.r, block.filled_color.g, block.filled_color.b),
                    (block._pos.x, block._pos.y, block._size.x, block._size.y)
                )


class DebugBlock():
    _size: Position
    _pos: Position
    filled_color: Color
    empty_color: Color
    value: None

    def __init__(self, size: Position, pos: Position, filled_color: Color, empty_color: Color):
        self._size = size
        self._pos = pos
        self.filled_color = filled_color
        self.empty_color = empty_color
        self.value = None
        
    def draw(self):
        # Draw block if it contains info
        if self.value:
            GUI_STATIC.active_screen.fill(
                (self.filled_color.r, self.filled_color.g, self.filled_color.b),
                (self._pos.x, self._pos.y, self._size.x, self._size.y)
            )
        # else:
        #     screen.fill(self.empty_color.as_tuple, (self._pos.as_tuple, self._size.as_tuple))


class DebugZonedGrid(ZonedGrid, DebugGrid):
    zones: list  # list(DebugZone)
    
    def draw(self):
        for zone in self.zones:
            zone.draw()

        super().draw()



class DebugZone(Zone, DebugZonedGrid):
    def draw(self):
        # TODO: Draw zone area with color,
        # depending whether it is empty or not

        super().draw()
