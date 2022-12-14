import pytest

from vectors import Vector
import show

def test_show():
    g = show.Grid(64, 64, scale=2)
    g.dot(Vector(8, 28))
    g.box(Vector(56, 56))
    g.line(Vector(8, 28), Vector(56, 56))

    g.dot(Vector(0, 0), size=10, color=show.BLUE)
    g.dot(Vector(64, 0), size=10, color=show.BLUE)
    g.pixel(64, 64)
    g.show()

