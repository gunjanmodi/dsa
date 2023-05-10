import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
        k = 2
        self.assertEqual(6, Solution().longestOnes(nums, k))

    def test_case_2(self):
        nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
        k = 3
        self.assertEqual(10, Solution().longestOnes(nums, k))


if __name__ == '__main__':
    unittest.main()
