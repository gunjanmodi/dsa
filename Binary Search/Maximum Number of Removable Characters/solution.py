from typing import List


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:  # noqa
        index_of_removable = {val: i for i, val in enumerate(removable)}

        def is_valid_subsequence_after_removal(k):
            i, j = 0, 0
            while i < len(s) and j < len(p):
                if i in index_of_removable and index_of_removable[i] <= k:
                    i += 1
                    continue
                if s[i] == p[j]:
                    j += 1
                i += 1
            return len(p) == j

        left = 0
        right = len(removable)

        while left < right:
            mid = left + (right - left) // 2
            if is_valid_subsequence_after_removal(mid):
                left = mid + 1
            else:
                right = mid
        return left
