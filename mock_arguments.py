import mock

class X(object):
    def m(self):
        return 'm'

def new_m(self, **kwargs):
    return 'new_m %s' % kwargs.items()

with mock.patch.object(X, 'm', 'new_m', a=1, b=2):
    print X().m()

