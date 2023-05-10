import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 4
        self.assertEqual(False, Solution().carPooling(trips, capacity))

    def test_case_2(self):
        trips = [[2, 1, 5], [3, 3, 7]]
        capacity = 5
        self.assertEqual(True, Solution().carPooling(trips, capacity))

    def test_case_3(self):
        trips = [[9, 3, 4], [9, 1, 7], [4, 2, 4], [7, 4, 5]]
        capacity = 23
        self.assertEqual(True, Solution().carPooling(trips, capacity))

    def test_case_4(self):
        trips = [[7, 5, 6], [6, 7, 8], [10, 1, 6]]
        capacity = 16
        self.assertEqual(False, Solution().carPooling(trips, capacity))

    def test_case_5(self):
        trips = [[7, 5, 6]]
        capacity = 11
        self.assertEqual(True, Solution().carPooling(trips, capacity))

    def test_case_6(self):
        trips = [[7, 5, 6]]
        capacity = 2
        self.assertEqual(False, Solution().carPooling(trips, capacity))

if __name__ == '__main__':
    unittest.main()
