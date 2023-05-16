import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        target = 12
        position = [10, 8, 0, 5, 3]
        speed = [2, 4, 1, 1, 3]
        expected = 3
        self.assertEqual(expected, Solution().carFleet(target, position, speed))

    def test_case_2(self):
        target = 10
        position = [3]
        speed = [3]
        expected = 1
        self.assertEqual(expected, Solution().carFleet(target, position, speed))

    def test_case_3(self):
        target = 100
        position = [0, 2, 4]
        speed = [4, 2, 1]
        expected = 1
        self.assertEqual(expected, Solution().carFleet(target, position, speed))

    def test_case_4(self):
        target = 50
        position = [0, 5, 10, 15, 20]
        speed = [5, 10, 15, 20, 25]
        expected = 5
        self.assertEqual(expected, Solution().carFleet(target, position, speed))


if __name__ == '__main__':
    unittest.main()
