from pprint import pprint

from pyparsing import Group
from pyparsing import oneOf
from pyparsing import Optional
from pyparsing import ZeroOrMore


region_atom = oneOf(['A', 'B', 'C', 'D', 'E'])
fill_operator = oneOf(['to'])
conjunction = oneOf([',', 'and'])


text = 'A and B to C, D and E'

expected = [
    [
        ['A', 'B'],
        ['to'],
        ['C'],
    ],
    'D',
    'E',
]


region = Group(region_atom + Optional(fill_operator + region_atom))
grammar = region + ZeroOrMore(conjunction + region)

print text
pprint(grammar.parseString(text).asList())
