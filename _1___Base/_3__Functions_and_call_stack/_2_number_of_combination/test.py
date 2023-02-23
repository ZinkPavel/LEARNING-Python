import unittest

from .number_of_combination import get_number_of_combination


class TestGetNumberOfCombination(unittest.TestCase):
    def test(self):
        self.assertEqual(get_number_of_combination(3, 2), 3)
        self.assertEqual(get_number_of_combination(10, 5), 252)


if __name__ == "__main__":
    unittest.main()
