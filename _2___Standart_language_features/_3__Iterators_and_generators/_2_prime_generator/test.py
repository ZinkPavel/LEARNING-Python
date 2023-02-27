from .generator import primes

import unittest
import itertools


class TestGenerator(unittest.TestCase):
    def test(self):
        self.assertListEqual(
            list(itertools.takewhile(lambda x: x <= 31, primes())),
            [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],
        )
