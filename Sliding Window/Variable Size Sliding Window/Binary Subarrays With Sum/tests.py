import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        nums = [1, 0, 1, 0, 1]
        goal = 2
        self.assertEqual(4, Solution().numSubarraysWithSum(nums, goal))

    def test_case_2(self):
        nums = [0, 0, 0, 0, 0]
        goal = 0
        self.assertEqual(15, Solution().numSubarraysWithSum(nums, goal))

    def test_case_3(self):
        nums = [1, 1, 1, 1, 1]
        goal = 5
        self.assertEqual(1, Solution().numSubarraysWithSum(nums, goal))

    def test_case_4(self):
        nums = [1, 0, 0, 0, 0, 1]
        goal = 1
        self.assertEqual(10, Solution().numSubarraysWithSum(nums, goal))

    def test_case_5(self):
        nums = [0, 0, 0]
        goal = 1
        self.assertEqual(0, Solution().numSubarraysWithSum(nums, goal))

    def test_case_6(self):
        nums = []
        goal = 0
        self.assertEqual(0, Solution().numSubarraysWithSum(nums, goal))


if __name__ == '__main__':
    unittest.main()
