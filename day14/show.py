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
        self.img = Image.new('RGBA', self.size, (0, 0, 0, 255))
        self.draw = ImageDraw.Draw(self.img)

    def _bounding_box(self, v0, v1):
        return (
            v0.x * self.scale,
            v0.y * self.scale,
            v1.x * self.scale,
            v1.y * self.scale,
        )

    def line(self, source: Vector, target: Vector, width=3, color=BLUE):
        self.draw.line(
            self._bounding_box(source, target),
            fill=color,
            width=width,
        )

    def dot(self, point, size=3, color=GREEN):
        point = point * self.scale
        offset = Vector(size * self.scale // 2, size * self.scale // 2)
        self.draw.ellipse(
            self._bounding_box(point - offset, point + offset),
            fill=color,
        )

    def box(self, point, size=4, color=RED):
        offset = Vector(size * self.scale // 2, size * self.scale // 2)
        self.draw.rounded_rectangle(
            self._bounding_box(point - offset, point + offset),
            radius=2,
            fill=color,
        )

    def show(self):
        self.img.show()
