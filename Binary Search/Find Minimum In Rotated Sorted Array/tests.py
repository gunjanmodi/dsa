import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_array_is_rotated_1(self):
        nums = [3, 4, 5, 1, 2]
        self.assertEqual(1, Solution().findMin(nums))

    def test_array_is_rotated_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        self.assertEqual(0, Solution().findMin(nums))

    def test_array_is_not_rotated(self):
        nums = [11, 13, 15, 17]
        self.assertEqual(11, Solution().findMin(nums))

    def test_all_elements_are_equal(self):
        nums = [4, 4, 4, 4]
        self.assertEqual(4, Solution().findMin(nums))

    def test_array_has_only_two_elements(self):
        nums = [2, 1]
        self.assertEqual(1, Solution().findMin(nums))

    def test_array_has_single_element(self):
        nums = [2]
        self.assertEqual(2, Solution().findMin(nums))


if __name__ == '__main__':
    unittest.main()
