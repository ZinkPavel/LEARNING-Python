import unittest

from .buffer import Buffer


class TestBuffer(unittest.TestCase):
    def setUp(self):
        self.buffer = Buffer()

    def test(self):
        self.buffer.add(1, 2, 3)
        self.assertEqual(self.buffer.get_current_part(), [1, 2, 3])  # вернуть [1, 2, 3]

        self.buffer.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
        self.assertEqual(self.buffer.get_current_part(), [6])  # вернуть [6]

        self.buffer.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
        self.assertEqual(self.buffer.get_current_part(), [])  # вернуть []

        self.buffer.add(
            1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
        )  # print(5), print(5) – вывод сумм третьей и четвертой пятерки
        self.assertEqual(self.buffer.get_current_part(), [1])  # вернуть [1]
