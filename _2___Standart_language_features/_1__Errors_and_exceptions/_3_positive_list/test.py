import unittest

from .positive_list import PositiveList, NonPositiveError


class TestPositiveList(unittest.TestCase):
    def setUp(self):
        self.l = PositiveList()

    def test(self):
        self.l.append(1)
        self.l.append(5)
        with self.assertRaises(NonPositiveError):
            self.l.append(0)
        self.assertListEqual(self.l, [1, 5])
