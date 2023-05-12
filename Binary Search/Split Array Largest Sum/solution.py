from typing import List


class Solution:
    """
    Problem: https://leetcode.com/problems/split-array-largest-sum

    Similar problem as Capacity To Ship Packages Within D Days.

    Time Complexity: O(n*log(sum(nums))), n is the length of the input list nums
    Space Complexity: O(1)
    """
    def splitArray(self, nums: List[int], k: int) -> int:  # noqa

        def condition(mid):
            number_of_subarrays = 1
            total = 0
            for num in nums:
                total += num
                if total > mid:
                    number_of_subarrays += 1
                    total = num
            return number_of_subarrays <= k

        """
        # p is number of pieces for a given largest_sum
        # For p = len(nums) the largest_sum is max(nums)
        # for p = 1 the largest_sum is sum(nums)
        # We are looking for p=k, as we go from p=1 to p=len(nums) the 
        # largest sum goes from max(nums) to sum(nums) - > search space
        """
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
