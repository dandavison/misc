class Pool(object):

    def __init__(self, *args, **kwargs):
        pass

    def apply_async(self, f, **kwargs):
        return f(*kwargs['args'], **kwargs['kwds'])

    def join(self):
        pass

    def close(self):
        pass

