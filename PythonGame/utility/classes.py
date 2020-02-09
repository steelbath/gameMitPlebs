

class Position(object):
    """Wrapper for two-dimensional positions with some extra functionality"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def get_angle_to(self, other_pos: Position) -> float:
        pass

    def get_angle_to_coords(self, x: int, y: int) -> float:
        return self.get_angle_to(Position(x, y))

    def get_distance_to(self, other_pos: Position) -> float:
        pass

    def get_distance_to_coords(self, x: int, y: int) -> float:
        return self.get_distance_to(Position(x, y))

    @classmethod
    def zero(cls) -> Position:
        return cls(0, 0)


class ColorMeta(type):
    """Meta class for color to allow quick hand colors
        such as `Color.white` returning white
    """
    @property
    def white(cls) -> Color:
        return cls(255, 255, 255)

    @property
    def black(cls) -> Color:
        return cls(0, 0, 0)

    @property
    def red(cls) -> Color:
        return cls(255, 0, 0)

    @property
    def green(cls) -> Color:
        return cls(0, 255, 0)

    @property
    def blue(cls) -> Color:
        return cls(0, 0, 255)


class Color(object, metaclass=ColorMeta):
    def __init__(self, r: int, g: int, b: int, a: int = 255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def get_as_tuple(self) -> tuple:
        return (self.r, self.g, self.b, self.a)

    def get_as_dict(self) -> dict:
        return {
            "red": self.r,
            "green": self.g,
            "blue": self.b,
            "alpha": self.a
        }
