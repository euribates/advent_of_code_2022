import re

from models import Monkey


pat_monkey = re.compile(r'Monkey (\d+):')  # Monkey 2:

pat_starting_items = re.compile(r'\s*Starting items: (.+)')  # Starting items: 79, 60, 97

pat_operation = re.compile(r'\s*Operation: new = (.+)')  # Operation: new = old + 3

pat_test = re.compile(r'\s*Test: divisible by (\d+)')  # Test: divisible by <int>

pat_if_true = re.compile(r'\s*If true: throw to monkey (\d+)')  # If true: throw to monkey <int>

pat_if_false = re.compile(r'\s*If false: throw to monkey (\d+)')  # If falsee: throw to monkey <int?


def parse_starting_items(source):
    num, line = next(source)
    _match = pat_starting_items.match(line)
    if _match:
        items = _match.group(1)
        if items.isdigit():
            return [int(items)]
        return [int(num) for num in items.split(',')]
    else:
        raise ValueError(f'parse_starting_items: Error al procesar linea {num}: {line}')


def parse_operation(source):
    num, line = next(source)
    _match = pat_operation.match(line)
    if _match:
        return _match.group(1)
    else:
        raise ValueError(f'parse_operation: Error al procesar linea {num}: {line}')
    
    
def parse_test(source):
    num, line = next(source)
    _match = pat_test.match(line)
    if _match:
        return int(_match.group(1))
    else:
        raise ValueError(f'parse_test: Error al procesar linea {num}: {line}')
    
def parse_if_true(source):
    num, line = next(source)
    _match = pat_if_true.match(line)
    if _match:
        return int(_match.group(1))
    else:
        raise ValueError(f'parse_if_true: Error al procesar linea {num}: {line}')
    
    
def parse_if_false(source):
    num, line = next(source)
    _match = pat_if_false.match(line)
    if _match:
        return int(_match.group(1))
    else:
        raise ValueError(f'parse_if_false: Error al procesar linea {num}: {line}')
    
    
def parse_monkey(source):    
    num, line = next(source)
    _match = pat_monkey.match(line)
    if _match:
        num = int(_match.group(1))
        starting_items = parse_starting_items(source)
        monkey = Monkey(num, starting_items)
        monkey.operation = parse_operation(source)
        monkey.test = parse_test(source)
        monkey.throw_if_true = parse_if_true(source)
        monkey.throw_if_false = parse_if_false(source)
        return monkey
    else:
        raise ValueError(f'parse_monkey: Error al procesar linea {num}: {line}')    
        
    
def parser(source):
    while True:
        try:
            monkey = parse_monkey(source)
            yield monkey
        except StopIteration:
            break
