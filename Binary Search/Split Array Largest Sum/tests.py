import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [7, 2, 5, 10, 8]
        k = 2
        expected = 18
        self.assertEqual(expected, Solution().splitArray(nums, k))

    def test_case_2(self):
        nums = [7, 2, 5, 10, 8]
        k = 2
        expected = 18
        self.assertEqual(expected, Solution().splitArray(nums, k))

    def test_case_3(self):
        nums = [7, 2, 5, 10, 8]
        k = 2
        expected = 18
        self.assertEqual(expected, Solution().splitArray(nums, k))

    def test_large_input(self):
        nums = [i for i in range(1000)]
        k = 50
        expected = 10335
        self.assertEqual(expected, Solution().splitArray(nums, k))

    def test_small_input(self):
        nums = [1]
        k = 1
        expected = 1
        self.assertEqual(expected, Solution().splitArray(nums, k))


if __name__ == '__main__':
    unittest.main()
