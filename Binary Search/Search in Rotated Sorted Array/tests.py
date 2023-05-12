import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_target_exists_1(self):
        nums = [5, 6, 7, 8, 1, 2, 3, 4]
        target = 2
        self.assertEqual(5, Solution().search(nums, target))

    def test_target_exists_2(self):
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        self.assertEqual(4, Solution().search(nums, target))

    def test_target_does_not_exists(self):
        nums = [5, 6, 7, 8, 1, 2, 3, 4]
        target = 10
        self.assertEqual(-1, Solution().search(nums, target))

    def test_target_exists_at_beginning_of_the_array(self):
        nums = [5, 6, 7, 8, 1, 2, 3, 4]
        target = 5
        self.assertEqual(0, Solution().search(nums, target))

    def test_target_exists_at_end_of_the_array(self):
        nums = [5, 6, 7, 8, 1, 2, 3, 4]
        target = 4
        self.assertEqual(7, Solution().search(nums, target))

    def test_array_with_single_element(self):
        nums = [4]
        target = 4
        self.assertEqual(0, Solution().search(nums, target))

    def test_array_with_empty_array(self):
        nums = []
        target = 2
        self.assertEqual(-1, Solution().search(nums, target))

    def test_all_elements_are_negative(self):
        nums = [-4, -3, -2, -1, -5]
        target = -5
        self.assertEqual(4, Solution().search(nums, target))


if __name__ == '__main__':
    unittest.main()
