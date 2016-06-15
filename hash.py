class Hashable(object):

    def __init__(self, data):
        self.data = data
    
    def __hash__(self):
        return self.data


print hash(Hashable(7))
