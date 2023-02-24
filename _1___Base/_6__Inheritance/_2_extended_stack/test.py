import unittest

from .extended_stack import ExtendedStack


class TestExtendedStack(unittest.TestCase):
    def setUp(self):
        self.stack = ExtendedStack()
        self.stack.extend(range(11))

    def test(self):
        self.stack.sum()
        self.assertEqual(self.stack[len(self.stack) - 1], 19)
        self.stack.sub()
        self.assertEqual(self.stack[len(self.stack) - 1], 11)
        self.stack.mul()
        self.assertEqual(self.stack[len(self.stack) - 1], 77)
        self.stack.div()
        self.assertEqual(self.stack[len(self.stack) - 1], 12)
