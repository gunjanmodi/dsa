import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "abcabcbb"
        self.assertEqual(3, Solution().lengthOfLongestSubstring(s))

    def test_case_2(self):
        s = "bbbbb"
        self.assertEqual(1, Solution().lengthOfLongestSubstring(s))


if __name__ == '__main__':
    unittest.main()
