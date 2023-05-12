import unittest
from solution import Solution


class TestSolution(unittest.TestCase):

    def test_case_1(self):
        s = "abcacb"
        p = "ab"
        removable = [3, 1, 0]
        self.assertEqual(2, Solution().maximumRemovals(s, p, removable))

    def test_case_2(self):
        s = "abcbddddd"
        p = "abcd"
        removable = [3, 2, 1, 4, 5, 6]
        self.assertEqual(1, Solution().maximumRemovals(s, p, removable))

    def test_case_3(self):
        s = "abcab"
        p = "abc"
        removable = [0, 1, 2, 3, 4]
        self.assertEqual(0, Solution().maximumRemovals(s, p, removable))

    def test_case_4(self):
        s = "rqmvwezfxczzeqokjww"
        p = "rezxczzeqw"
        removable = [18, 1, 3, 7, 4, 16, 14, 2, 15, 0, 6, 12, 17, 11, 13, 5, 9]
        self.assertEqual(9, Solution().maximumRemovals(s, p, removable))


if __name__ == '__main__':
    unittest.main()
