from typing import List


class Solution:
    """
    Problem Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

    Explanation: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/solutions/158940/beat-100-very-simple-python-very-detailed-explanation/?orderBy=most_votes # noqa

    Time complexity: O(log n)
    Space complexity: O(1)
    """
    def findMin(self, nums: List[int]) -> int: # noqa

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = left + (right - left) // 2

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
