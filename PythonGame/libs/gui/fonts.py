
from pygame import font


class Font(object):
    name = None  # Default font
    size = 24
    bold = False
    italic = False

    def build_font(self) -> font.Font:
        return font.SysFont(self.name, self.size, self.bold, self.italic)

    def set_size(self, size):
        self.size = size


class TimesRoman(Font):
    name = "times.ttf"


class Arial(Font):
    name = "arial.ttf"
