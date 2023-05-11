import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_target_element_is_present_in_the_array(self):
        nums = [1, 3, 5, 6]
        target = 5
        self.assertEqual(2, Solution().searchInsert(nums, target))

    def test_target_element_not_present_in_array_and_can_be_inserted_at_the_beginning(self):
        nums = [1, 3, 5, 6]
        target = 0
        self.assertEqual(0, Solution().searchInsert(nums, target))

    def test_target_element_not_present_in_array_and_can_be_inserted_at_the_end(self):
        nums = [1, 3, 5, 6]
        target = 7
        self.assertEqual(4, Solution().searchInsert(nums, target))

    def test_target_element_is_not_present_in_the_array_but_can_be_inserted_in_between_the_elements(self):
        nums = [1, 3, 5, 6]
        target = 4
        self.assertEqual(2, Solution().searchInsert(nums, target))

    def test_target_element_is_smaller_than_the_first_element_in_the_array(self):
        nums = [1, 3, 5, 6]
        target = -2
        self.assertEqual(0, Solution().searchInsert(nums, target))

    def test_target_element_is_larger_than_the_last_element_in_the_array(self):
        nums = [1, 3, 5, 6]
        target = 8
        self.assertEqual(4, Solution().searchInsert(nums, target))

    def test_array_contains_only_one_element_and_the_target_element_is_greater_than_that(self):
        nums = [1]
        target = 2
        self.assertEqual(1, Solution().searchInsert(nums, target))

    def test_array_contains_only_one_element_and_the_target_element_is_smaller_than_that(self):
        nums = [2]
        target = 1
        self.assertEqual(0, Solution().searchInsert(nums, target))


if __name__ == '__main__':
    unittest.main()
