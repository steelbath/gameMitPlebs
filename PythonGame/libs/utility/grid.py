
import math

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

    def __init__(self, width, height, pos, size):
        self.width = width
        self.height = height
        self._pos = Position(pos.x, pos.y)
        self._size = Position(size.x, size.y)
        self.blocks = list(width * height)
        self._block_size = Position(
            size.x / width,
            size.y / height
        )

    def get_block_at(self, pos: Position, relative=False):
        pass

    def get_block_towards(self, pos: Position, Direction: Direction, relative=False):
        pass

    def get_blocks_in_circle(self, pos: Position, radius: float, relative=False):
        pass

    def get_blocks_in_square(self, pos: Position, size: Position, relative=False):
        pass


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
        size = self._block_size
        for x in range(0, self.width * self.height):
            pos = Position(
                (1 + x % self.width) * self._block_size.x,
                math.floor(x / self.width) * self._block_size.y
            )
            self.blocks.push(DebugBlock(self._block_size, pos, filled_color, empty_color))
            
    def draw():
        for block in self.blocks:
            block.draw()


class DebugBlock():
    _size: Position
    _pos: Position
    filled_color: Color
    empty_color: Color

    def __init__(self, size: Position, pos: Position, filled_color: Color, empty_color: Color):
        self._size = size
        self._pos = pos
        self.filled_color = filled_color
        self.empty_color = empty_color
        
    def draw():
        # TODO: Draw block if it contains info

        pass


class DebugZonedGrid(ZonedGrid, DebugGrid):
    zones: list(DebugZone)
    
    def draw():
        for zone in self.zones:
            zone.draw()

        super().draw()



class DebugZone(Zone, DebugZonedGrid):
    def draw():
        # TODO: Draw zone area with color,
        # depending whether it is empty or not

        super().draw()
