from collections import deque

import pytest

import parser


REGEX_TESTS = [
    (parser.pat_monkey, 'Monkey 23:', '23'),
    (parser.pat_starting_items, 'Starting items: 79, 60, 97', '79, 60, 97'),
    (parser.pat_starting_items, 'Starting items: 32', '32'),
    (parser.pat_operation, 'Operation: new = old + 1', 'old + 1'),
    (parser.pat_operation, 'Operation: new = old * 7', 'old * 7'),
    (parser.pat_operation, 'Operation: new = old / 2', 'old / 2'),
    (parser.pat_operation, 'Operation: new = old - 4',  'old - 4'),
    (parser.pat_operation, 'Operation: new = old + old', 'old + old'),
    (parser.pat_test, 'Test: divisible by 12', '12'),
    (parser.pat_if_true, 'If true: throw to monkey 13', '13'),
    (parser.pat_if_false, 'If false: throw to monkey 15', '15'),
]


@pytest.mark.parametrize("patron, input_string, expected", REGEX_TESTS)
def test_regular_expressions(patron, input_string, expected):
    assert patron.match(input_string).group(1) == expected


def test_parse_starting_items():
    src = iter([
        (0, 'Starting items: 54, 65, 75, 74'),
    ])
    assert parser.parse_starting_items(src) == [54, 65, 75, 74]


def test_parse_starting_items_just_one():
    src = iter([
        (0, 'Starting items: 77'),
    ])
    assert parser.parse_starting_items(src) == [77]


def test_parse_operation():
    src = iter([
        (0, 'Operation: new = old * 19'),
    ])
    assert parser.parse_operation(src) == 'old * 19'
    

def test_parse_test():
    src = iter([
        (0, 'Test: divisible by 98'),
    ])
    assert parser.parse_test(src) == 98


def test_parse_if_true():
    src = iter([
        (0, 'If true: throw to monkey 17'),
    ])
    assert parser.parse_if_true(src) == 17
    

def test_parse_if_false():
    src = iter([
        (0, 'If false: throw to monkey 15'),
    ])
    assert parser.parse_if_false(src) == 15


def test_parse_monkey():
    src = iter([
        (0, 'Monkey 2:'),
        (1, '  Starting items: 79, 60, 97'),
        (2, '  Operation: new = old * old'),
        (3, '  Test: divisible by 13'),
        (4, '    If true: throw to monkey 1'),
        (5, '    If false: throw to monkey 3'),
    ])
    monkey = parser.parse_monkey(src)
    assert monkey.num == 2
    assert monkey.items == deque([79, 60, 97])
    assert monkey.operation == 'old * old'
    assert monkey.test == 13
    assert monkey.throw_if_true == 1
    assert monkey.throw_if_false == 3

def test_parser():
    with open('sample.txt', 'r') as f_input:
        monkeys = list(parser.parser(
            (line_num, line.strip())
            for (line_num, line) in enumerate(f_input)
            if line.strip()
        ))
        assert len(monkeys) == 4
        assert monkeys[0].num == 0
        assert monkeys[1].num == 1
        assert monkeys[2].num == 2
        assert monkeys[3].num == 3

