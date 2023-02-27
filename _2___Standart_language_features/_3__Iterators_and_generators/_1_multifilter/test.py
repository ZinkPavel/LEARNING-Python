from .multifilter import multifilter

import unittest


def mul2(x):
    return x % 2 == 0


def mul3(x):
    return x % 3 == 0


def mul5(x):
    return x % 5 == 0


class TestMultifilter(unittest.TestCase):
    def test_0(self):
        a = [i for i in range(11)]
        self.assertListEqual(
            list(multifilter(a, mul2, mul3, mul5)),
            [0, 2, 3, 4, 5, 6, 8, 9, 10],
        )

    def test_1(self):
        a = [i for i in range(31)]
        self.assertListEqual(
            list(multifilter(a, mul2, mul3, mul5)),
            [
                0,
                2,
                3,
                4,
                5,
                6,
                8,
                9,
                10,
                12,
                14,
                15,
                16,
                18,
                20,
                21,
                22,
                24,
                25,
                26,
                27,
                28,
                30,
            ],
        )
