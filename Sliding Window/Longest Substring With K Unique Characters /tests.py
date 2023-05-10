import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        s = "aabacbebebe"
        k = 3
        self.assertEqual(7, Solution().longestSubstringWithKUniqueCharacters(s, k))

    def test_case_2(self):
        s = "aaaa"
        k = 2
        self.assertEqual(-1, Solution().longestSubstringWithKUniqueCharacters(s, k))

    def test_case_3(self):
        s = "gbwkfnqduxwfn"
        k = 15
        self.assertEqual(-1, Solution().longestSubstringWithKUniqueCharacters(s, k))


if __name__ == '__main__':
    unittest.main()
