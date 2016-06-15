def f():
    a = []
    b = 1
    class X(object):

        @staticmethod
        def append():
            a.append(1)

        @staticmethod
        def show():
            print a

    return X


cls = f()
cls.show()
cls.append()
cls.show()
