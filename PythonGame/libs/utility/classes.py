
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
        return self - other_pos

    def floor(self):
        self.x = math.floor(self.x)
        self.y = math.floor(self.y)
        return self
    
    def ceil(self):
        self.x = math.ceil(self.x)
        self.y = math.ceil(self.y)
        return self

    def round(self):
        self.x = round(self.x)
        self.y = round(self.y)
        return self

    @property
    def as_tuple(self):
        return (self.x, self.y)
    
    # Override how this object is printed out
    def __str__(self):
        return "Position (%s, %s)" % (self.x, self.y)

    # Override how this object is printed out
    def __repr__(self):
        return "Position (%s, %s)" % (self.x, self.y)


class ColorMeta(type):
    """Meta class for color to allow quick hand colors
        such as `Color.white` returning white
    """
    @property
    def white(cls) -> 'Color':
        return cls(255, 255, 255)

    @property
    def light_grey(cls) -> 'Color':
        return cls(190, 190, 190)

    @property
    def grey(cls) -> 'Color':
        return cls(127, 127, 127)

    @property
    def dark_grey(cls) -> 'Color':
        return cls(65, 65, 65)

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

    def clone(self):
        return Color(self.r, self.g, self.b, self.a)

    def darken(self):
        # FIXME: Stupid implementation
        self.r = max(self.r - 40, 0)
        self.g = max(self.g - 40, 0)
        self.b = max(self.b - 40, 0)
        self.a = max(self.a - 40, 0)
        return self

    def lighten(self):
        # FIXME: Stupid implementation
        self.r = min(self.r + 40, 255)
        self.g = min(self.g + 40, 255)
        self.b = min(self.b + 40, 255)
        self.a = min(self.a + 40, 255)
        return self

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
