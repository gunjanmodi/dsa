import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_1(self):
        asteroids = [5, 10, -5]
        expected = [5, 10]
        self.assertEqual(expected, Solution().asteroidCollision(asteroids))

    def test_case_2(self):
        asteroids = [8, -8]
        expected = []
        self.assertEqual(expected, Solution().asteroidCollision(asteroids))

    def test_case_3(self):
        asteroids = [10, 2, -5]
        expected = [10]
        self.assertEqual(expected, Solution().asteroidCollision(asteroids))

    def test_case_4(self):
        asteroids = [-5, 10, 5, -8, 3, -3, -1, 7, 2, -4, 6, 9]
        expected = [-5, 10, 7, 6, 9]
        self.assertEqual(expected, Solution().asteroidCollision(asteroids))

    def test_case_5(self):
        asteroids = [-2, -2, 1, 1, -2]
        expected = [-2, -2, -2]
        self.assertEqual(expected, Solution().asteroidCollision(asteroids))

    def test_case_6(self):
        asteroids = [-2, -1, 1, -2]
        expected = [-2, -1, -2]
        self.assertEqual(expected, Solution().asteroidCollision(asteroids))

    def test_case_7(self):
        asteroids = [-2, -2, 1, -1]
        expected = [-2, -2]
        self.assertEqual(expected, Solution().asteroidCollision(asteroids))

    def test_case_8(self):
        asteroids = [1, -2, -2, -2]
        expected = [-2, -2, -2]
        self.assertEqual(expected, Solution().asteroidCollision(asteroids))


if __name__ == '__main__':
    unittest.main()
