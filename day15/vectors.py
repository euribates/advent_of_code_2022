from dataclasses import dataclass


@dataclass(frozen=True)
class Vector():
    x: int = 0
    y: int = 0

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)