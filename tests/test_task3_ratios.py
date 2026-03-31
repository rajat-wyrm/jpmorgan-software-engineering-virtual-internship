import unittest

class TestTask3Ratios(unittest.TestCase):
    def test_upper_lower_sum(self):
        upper, lower = 0.6, 0.4
        self.assertAlmostEqual(upper + lower, 1.0)
