
import math


class PositionMeta(type):
    """Meta class for color to allow quick hand colors
        such as `Position.zero` returning zero position
    """
    @property
    def zero(cls) -> 'Position':
        return cls(0, 0)


class Position(object, metaclass=PositionMeta):
    """Wrapper for two-dimensional positions with some extra functionality"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    # Operator overloading, to allow basic arithmetic operations with positions
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __idiv__(self, other):
        self.x /= other.x
        self.y /= other.y
        return self

    def __add__(self, other):
        return Position(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Position(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Position(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Position(self.x / other.x, self.y / other.y)
    
    def get_coords_to_distance_and_angle(self, distance: float, angle: float) -> 'Position':
        x = math.sin(math.radians(angle)) * distance
        y = math.cos(math.radians(angle)) * distance
        return self + Position(x, y)

    def get_angle_to(self, other_pos: 'Position') -> float:
        """Return angle in degrees, from point A to B"""
        raise NotImplementedError("TODO: Unfinished feature")

    def get_angle_to_coords(self, x: int, y: int) -> float:
        return self.get_angle_to(Position(x, y))

    def get_distance_to(self, other_pos: 'Position') -> float:
        """Return distance from point A to B"""
        return math.sqrt(self.x * self.x + self.y * self.y)

    def get_distance_to_coords(self, x: int, y: int) -> float:
        return self.get_distance_to(Position(x, y))

    def normalize_to(self, other_pos) -> 'Position':
        normal_x = self.x - other_pos.x
        normal_y = self.y - other_pos.y
        return Position(normal_x, normal_y)

    @property
    def as_tuple(self):
        return (self.x, self.y)


class ColorMeta(type):
    """Meta class for color to allow quick hand colors
        such as `Color.white` returning white
    """
    @property
    def white(cls) -> 'Color':
        return cls(255, 255, 255)

    @property
    def black(cls) -> 'Color':
        return cls(0, 0, 0)

    @property
    def red(cls) -> 'Color':
        return cls(255, 0, 0)

    @property
    def green(cls) -> 'Color':
        return cls(0, 255, 0)

    @property
    def blue(cls) -> 'Color':
        return cls(0, 0, 255)


class Color(object, metaclass=ColorMeta):
    def __init__(self, r: int, g: int, b: int, a: int = 255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    @property
    def as_tuple(self) -> tuple:
        return (self.r, self.g, self.b, self.a)

    @property
    def as_dict(self) -> dict:
        return {
            "red": self.r,
            "green": self.g,
            "blue": self.b,
            "alpha": self.a
        }
