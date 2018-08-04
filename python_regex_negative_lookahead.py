#!/usr/bin/env python3

import re

bad_strings = [
    '',
    'N/A\r\nN/A',
    '\n',
    'N/A; N/A; N/A',
    'n/a',
    ' \r\n',
    '\n\n',
    'N/A; N/A',
    'n/a\r\nn/a\r\nn/a; n/a\r\nn/a\r\nn/a; n/a\r\nn/a\r\nn/a',
    'N/a\r\n',
    'n/a\r\nn/a; n/a\r\nn/a',
    ' ',
    'N/AN/A; N/AN/A',
    'n/a\nn/a',
    ' n/a',
    'n/A',
    'N/A\r\nN/A; N/A\r\nN/A',
    '\n\n\n',
    'n/a\r\n',
    '  ',
    'N/A',
    'N/A ',
    'n/a\r\nn/a\r\nn/a\r\nn/a; n/a\r\nn/a\r\nn/a\r\nn/a',
    'n/a ',
    'n/a; n/a',
    'n/a; n/a; n/a',
    'N/A\r\nN/A\r\nN/A\r\nN/A; N/A\r\nN/A\r\nN/A\r\nN/A',
    'n/an/a; n/an/a',
    'n/a\r\nn/a',
    'N/a',
    '\r\n',
    '\n\n\n\n\n',
    'N/A\r\n',
    'N/A\r\nN/A\r\nN/A; N/A\r\nN/A\r\nN/A; N/A\r\nN/A\r\nN/A',
]

good_strings = ['a', 'b', 'bb',
                'a ', ' a',
                'a;a', 'a;', 'a; ', ' ; a',
                'an/a', 'n/ab', 'n/a a']

def test(regex):
    bad_matches = [s for s in bad_strings if re.match(regex, s)]
    good_non_matches = [s for s in good_strings if not re.match(regex, s)]

    if bad_matches:
        print('Incorrectly matched:')
        for s in bad_matches:
            print('\t' + repr(s))

    if good_non_matches:
        print('Incorrectly failed to match:')
        for s in good_non_matches:
            print('\t' + repr(s))
