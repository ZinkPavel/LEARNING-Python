import unittest

from .closest_mod_5 import closest_mod_5


class TestClosestMod5(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_mod_5(5), 5)
        self.assertEqual(closest_mod_5(8), 10)


if __name__ == "__main__":
    unittest.main()
