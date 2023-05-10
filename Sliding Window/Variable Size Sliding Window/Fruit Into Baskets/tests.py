import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        fruits = [1, 2, 1]
        self.assertEqual(3, Solution().totalFruit(fruits))

    def test_case_2(self):
        fruits = [0, 1, 2, 2]
        self.assertEqual(3, Solution().totalFruit(fruits))

    def test_case_3(self):
        fruits = [1, 2, 3, 2, 2]
        self.assertEqual(4, Solution().totalFruit(fruits))

    def test_case_4(self):
        fruits = [0]
        self.assertEqual(1, Solution().totalFruit(fruits))


if __name__ == '__main__':
    unittest.main()
