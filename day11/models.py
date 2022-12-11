from functools import cache
from collections import deque


class Monkey:
    
    def __init__(self, num, items=None):
        self.num = num
        self.items = deque([] if items is None else list(items))
        self.operation = ''
        self.test = None
        self.throw_if_true = None
        self.throw_if_false = None
        self.num_checks = 0
        
    def __repr__(self):
        return f"Monkey({self.num}, items=[{','.join([str(num) for num in self.items])}])"
    
    @cache
    def make_test(self, value):
        return (value % self.test) == 0
        

