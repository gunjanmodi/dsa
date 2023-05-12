import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_multiple_occurrence_of_element(self):
        nums = [5, 7, 7, 8, 8, 10]
        target = 8
        self.assertListEqual([3, 4], Solution().searchRange(nums, target))

    def test_target_not_found_in_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 8]
        target = 9
        self.assertListEqual([-1, -1], Solution().searchRange(nums, target))

    def test_array_is_empty(self):
        nums = []
        target = 0
        self.assertListEqual([-1, -1], Solution().searchRange(nums, target))

    def test_target_found_at_start_of_the_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 8]
        target = 1
        self.assertListEqual([0, 0], Solution().searchRange(nums, target))

    def test_target_found_at_end_of_the_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7, 8]
        target = 8
        self.assertListEqual([11, 11], Solution().searchRange(nums, target))

    def test_single_element_in_the_array(self):
        nums = [3]
        target = 3
        self.assertListEqual([0, 0], Solution().searchRange(nums, target))


if __name__ == '__main__':
    unittest.main()
