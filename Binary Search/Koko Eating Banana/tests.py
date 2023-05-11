import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_single_pile_of_banana(self):
        piles = [10]
        h = 3
        self.assertEqual(4, Solution().minEatingSpeed(piles, h))

    def test_multiple_piles_of_banana_1(self):
        piles = [30, 11, 23, 4, 20]
        h = 5
        self.assertEqual(30, Solution().minEatingSpeed(piles, h))

    def test_multiple_piles_of_banana_2(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(23, Solution().minEatingSpeed(piles, h))

    def test_multiple_piles_of_banana_3(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(23, Solution().minEatingSpeed(piles, h))


if __name__ == '__main__':
    unittest.main()
