import unittest
from multiply import multiply


class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        test_x = 5
        test_y = 10
        self.assertEqual(multiply(test_x, test_y), 50, "should be 50")


if __name__ == '__main__':
    unittest.main()
