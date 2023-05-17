import unittest
from solution import Solution

class TestSolution(unittest.TestCase):
    def test_case_1(self):
        path = "/home/"
        expected = "/home"
        self.assertEqual(expected, Solution().simplifyPath(path))

    def test_case_2(self):
        path = "/../"
        expected = "/"
        self.assertEqual(expected, Solution().simplifyPath(path))

    def test_case_3(self):
        path = "/home//foo/"
        expected = "/home/foo"
        self.assertEqual(expected, Solution().simplifyPath(path))

    def test_case_4(self):
        path = "/../home/library//Downloads/../_/"
        expected = "/home/library/_"
        self.assertEqual(expected, Solution().simplifyPath(path))








if __name__ == '__main__':
    unittest.main()
