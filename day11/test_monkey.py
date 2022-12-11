#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

import pytest

from models import Monkey


def test_create_a_monkey():
    m = Monkey(0, items=(79, 98))
    m.operation = 'old * 19'
    m.test = 23
    m.throw_if_true = 2
    m.throw_if_false = 3
    assert m.num == 0
    assert m.items.popleft() == 79
    assert m.items.popleft() == 98
    assert len(m.items) == 0
