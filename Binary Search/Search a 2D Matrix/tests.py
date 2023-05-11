import unittest
from solution import Solution


class TestSolution(unittest.TestCase):
    def test_target_present_in_matrix(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        target = 16
        self.assertEqual(True, Solution().searchMatrixOptimizedApproach(matrix, target))
        self.assertEqual(True, Solution().searchMatrixIntuitionBasedApproach(matrix, target))
        self.assertEqual(True, Solution().searchMatrixTemplateBasedApproach(matrix, target))

    def test_target_not_present_in_matrix(self):
        matrix = [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 60]
        ]
        target = 13
        self.assertEqual(False, Solution().searchMatrixOptimizedApproach(matrix, target))
        self.assertEqual(False, Solution().searchMatrixIntuitionBasedApproach(matrix, target))
        self.assertEqual(False, Solution().searchMatrixTemplateBasedApproach(matrix, target))

    def test_single_row_matrix_matrix(self):
        matrix = [
            [1, 3, 5, 7]
        ]
        target = 3
        self.assertEqual(True, Solution().searchMatrixOptimizedApproach(matrix, target))
        self.assertEqual(True, Solution().searchMatrixIntuitionBasedApproach(matrix, target))
        self.assertEqual(True, Solution().searchMatrixTemplateBasedApproach(matrix, target))

    def test_single_column_matrix_matrix(self):
        matrix = [
            [1],
            [2],
            [3]
        ]
        target = 2
        self.assertEqual(True, Solution().searchMatrixOptimizedApproach(matrix, target))
        self.assertEqual(True, Solution().searchMatrixIntuitionBasedApproach(matrix, target))
        self.assertEqual(True, Solution().searchMatrixTemplateBasedApproach(matrix, target))

    def test_empty_matrix(self):
        matrix = []
        target = 2
        self.assertEqual(False, Solution().searchMatrixOptimizedApproach(matrix, target))
        self.assertEqual(False, Solution().searchMatrixIntuitionBasedApproach(matrix, target))
        self.assertEqual(False, Solution().searchMatrixTemplateBasedApproach(matrix, target))


if __name__ == '__main__':
    unittest.main()
