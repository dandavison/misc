from mock import Mock


class Spec(object):
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

m = Mock(a=1, b=2, spec_set=Spec(3, 4))  # works
m = Mock(a=1, b=2, spec_set={'a', 'b'})  # AttributeError: Mock object has no attribute 'a'
m = Mock(a=1, b=2, spec_set=['a', 'b'])  # works
