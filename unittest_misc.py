import unittest


def f():
    # raise ValueError
    pass


class TestCase(unittest.TestCase):
    def test(self):
        with self.assertRaises(ValueError, msg="message"):
            f()
        # self.assertRaises(ValueError, f, msg="message")
        self.assertEqual(1, 2, msg="Test 1 == 2")
        self.assertEqual(1, 3, msg="Test 1 == 3")


if __name__ == '__main__':
    unittest.main()
