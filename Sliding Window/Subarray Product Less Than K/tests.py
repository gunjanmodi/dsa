import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [10, 5, 2, 6]
        k = 100
        self.assertEqual(8, Solution().numSubarrayProductLessThanK(nums, k))

    def test_case_2(self):
        nums = [1, 2, 3]
        k = 0
        self.assertEqual(0, Solution().numSubarrayProductLessThanK(nums, k))

    def test_case_3(self):
        nums = [10, 9, 10, 4, 3, 8, 3, 3, 6, 2, 10, 10, 9, 3]
        k = 19
        self.assertEqual(18, Solution().numSubarrayProductLessThanK(nums, k))


if __name__ == '__main__':
    unittest.main()
