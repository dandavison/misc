#!/usr/bin/env python

from predicate import P
from predicate.predicate import get_values_list


class X(object):

    @property
    def prop_foo(self):
        return 'prop-val'

    @property
    def prop__foo(self):
        return 'prop-val'

x = X()


p1 = P(prop_foo='prop-val')
print x in p1  # => True

p2 = P(prop__foo='prop-val')
# print x in p2  # predicate.predicate.LookupNotFound: (LookupComponent('prop'), <__main__.X object at 0x10de18590>)

print get_values_list(x, 'prop_foo', 'xxx')
