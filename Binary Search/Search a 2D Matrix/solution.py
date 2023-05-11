from typing import List


class Solution:

    def searchMatrixIntuitionBasedApproach(self, matrix: List[List[int]], target: int) -> bool:  # noqa
        if not matrix:
            return False
        rows_size = len(matrix)
        columns_size = len(matrix[0])

        left = 0
        right = rows_size * columns_size - 1

        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // columns_size][mid % columns_size] >= target:
                right = mid
            else:
                left = mid + 1
        return matrix[left // columns_size][left % columns_size] == target

    def searchMatrixOptimizedApproach(self, matrix: List[List[int]], target: int) -> bool:  # noqa
        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            current = matrix[row][col]
            if current == target:
                return True
            elif target < current:
                col -= 1
            else:
                row += 1
        return False

    def searchMatrixTemplateBasedApproach(self, matrix: List[List[int]], target: int) -> bool:  # noqa
        if not matrix:
            return False
        rows_size = len(matrix)
        columns_size = len(matrix[0])

        left = 0
        right = rows_size * columns_size - 1

        while left < right:
            mid = left + (right - left) // 2
            if matrix[mid // columns_size][mid % columns_size] >= target:
                right = mid
            else:
                left = mid + 1
        return matrix[left // columns_size][left % columns_size] == target
