from .increment_data import increment_days_to_date

import unittest
import datetime


class TestIncrementData(unittest.TestCase):
    def test(self):
        self.assertEqual(
            increment_days_to_date(2015, 1, 1, 3), datetime.date(2015, 1, 4)
        )
        self.assertEqual(
            increment_days_to_date(2015, 1, 1, 150), datetime.date(2015, 5, 31)
        )
