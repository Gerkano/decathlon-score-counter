import unittest
from utils import convert_timestamp_to_float
from decathlon_rules import PointCounter

class TestScoreCalc(unittest.TestCase):

    def test_convert_timestamp_to_float(self):
        result = convert_timestamp_to_float("10.57.32")
        self.assertEqual(result, 657.32)

    def test_point_count(self):
        test_result = ["13.43", "4.35", "8.64", "1.50", "66.06", "19.05", "24.89", "2.20", "33.48", "6.51.01"]
        counter = PointCounter(test_result)
        self.assertEqual(counter.point_count(), 3099)

