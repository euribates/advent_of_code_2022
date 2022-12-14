import pytest

from vectors import Vector
import show

def test_show():
    g = show.Grid(64, 64, scale=2)
    g.dot(Vector(8, 8))
    g.box(Vector(56, 56))
    g.line(Vector(8, 8), Vector(56, 56))
    g.show()
