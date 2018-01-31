#!/usr/bin/env python

from django.utils.functional import cached_property

class X(object):

    @cached_property
    def cp(self):
        return self._compute_cp()

    @property
    def p(self):
        return self._compute_p()

    def _compute_cp(self):
        print 'computing cp'
        return 'cp_value'

    def _compute_p(self):
        print 'computing p'
        return 'p_value'

