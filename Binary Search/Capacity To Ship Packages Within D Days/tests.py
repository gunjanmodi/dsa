import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        days = 5
        expected = 15
        self.assertEqual(expected, Solution().shipWithinDays(weights, days))

    def test_case_2(self):
        weights = [3, 2, 2, 4, 1, 4]
        days = 3
        expected = 6
        self.assertEqual(expected, Solution().shipWithinDays(weights, days))

    def test_case_3(self):
        weights = [1, 2, 3, 1, 1]
        days = 4
        expected = 3
        self.assertEqual(expected, Solution().shipWithinDays(weights, days))


if __name__ == '__main__':
    unittest.main()
