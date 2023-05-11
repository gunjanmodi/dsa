import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_case_target_in_middle_of_the_array(self):
        nums = [1, 2, 3, 4, 5, 6, 7]
        target = 4
        self.assertEqual(3, Solution().search(nums, target))

    def test_case_target_at_beginning_of_the_array(self):
        nums = [2, 4, 6, 8, 10]
        target = 2
        self.assertEqual(0, Solution().search(nums, target))

    def test_case_target_at_end_of_the_array(self):
        nums = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 15
        self.assertEqual(7, Solution().search(nums, target))

    def test_case_target_not_present_in_the_array(self):
        nums = [1, 3, 5, 7, 9, 11, 13, 15]
        target = 8
        self.assertEqual(-1, Solution().search(nums, target))

    def test_case_single_element_in_the_array(self):
        nums = [4]
        target = 4
        self.assertEqual(0, Solution().search(nums, target))

    def test_case_array_is_empty(self):
        nums = []
        target = 4
        self.assertEqual(-1, Solution().search(nums, target))


if __name__ == '__main__':
    unittest.main()
