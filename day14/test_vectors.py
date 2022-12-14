import pytest

from vectors import Vector


def test_sub_vector():
    v1 = Vector(-1, -1)
    v2 = Vector(0, 2)
    assert v2 - v1 == Vector(1, 3)
    

def test_add_vector():
    v1 = Vector(-1, -1)
    v2 = Vector(0, 2)
    assert v2 + v1 == Vector(-1, 1)
    
       
def test_sub_vector2():
    v1 = Vector(-1, -1)
    v2 = Vector(0, 2)
    assert v2 - v1 == Vector(1, 3)
    

def test_vector2_is_hashable():
    v1 = Vector(-1, -1)
    v2 = Vector(0, 2)
    set([v1, v2])
    

def test_vector2_unary_minus():
    v = Vector(5, -2)
    assert -v == Vector(-5, 2)