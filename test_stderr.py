import unittest


class TestCase(unittest.TestCase):

    def test(self):
        print 'hello'
        self.assertTrue(False)
        print 'bye'


if __name__ == '__main__':
    unittest.main()
