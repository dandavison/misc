from pyparsing import *


text = "Angola and Namibia east to northeastern South Africa; Mozambique north to Kenya; Uganda"

REGION_NAMES = ['angola', 'namibia', 'south africa', 'kenya', 'uganda']
COMPASS_ADJECTIVES = ['northern', 'eastern', 'southern', 'western', 'northeastern', 'northwestern', 'southeastern', 'southwestern']
CONJUNCTIONS = ['and', 'east to', 'north to']

region_atom = oneOf(REGION_NAMES, caseless=True)
compass_adjective = oneOf(COMPASS_ADJECTIVES, caseless=True)
conjunction = oneOf(CONJUNCTIONS, caseless=True)


def grammar1():
    region = Group(Optional(compass_adjective) + region_atom)
    region_set = region + ZeroOrMore(conjunction + region)
    grammar = delimitedList(Group(region_set), delim=';')
    return grammar



print text
print grammar1().parseString(text)
