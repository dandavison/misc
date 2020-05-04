class classproperty(object):
    def __init__(self, method=None):
        self.fget = method

    def __get__(self, instance, cls=None):
        return self.fget(cls)

    def getter(self, method):
        self.fget = method
        return self


class X:
    name = None

    @classproperty
    def name(cls):
        import ipdb ; ipdb.set_trace()
        return cls.__getattribute__('name') or 'fallback name'



print(X.name)
