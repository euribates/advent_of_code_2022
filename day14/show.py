from PIL import Image, ImageDraw

from vectors import Vector

RED = (250, 100, 100)
GREEN = (100, 250, 100)
BLUE = (100, 100, 250)


class Grid:

    def __init__(self, width, height, scale=1):
        self.scale = scale
        self.width = width * scale
        self.height = height * scale
        self.size = (self.width, self.height)
        self.img = Image.new('RGBA', self.size, (32, 32, 32, 255))
        self.draw = ImageDraw.Draw(self.img)

    def _bounding_box(self, v0, v1):
        return (
            v0.x,
            v0.y,
            v1.x,
            v1.y,
        )

    def pixel(self, x, y, color=GREEN):
        self.draw.rectangle(
            (x-1, y-1, x+1, y+1),
            fill=color,
        )
    
    def line(self, source: Vector, target: Vector, width=3, color=BLUE):
        self.draw.line(
            self._bounding_box(source, target),
            fill=color,
            width=width,
        )

    def dot(self, point, size=3, color=GREEN):
        offset = Vector(min(size // 2, 1), min(size // 2, 1))
        self.draw.ellipse(
            self._bounding_box(point - offset, point + offset),
            fill=color,
        )

    def box(self, point, size=4, color=RED):
        offset = Vector(max(size // 2, 1), max(size // 2, 1))
        self.draw.rounded_rectangle(
            self._bounding_box(point - offset, point + offset),
            radius=2,
            fill=color,
        )

    def show(self):
        self.img.show()
