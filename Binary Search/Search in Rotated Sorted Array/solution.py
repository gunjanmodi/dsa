from typing import List


class Solution:
    """
    Problem link: https://leetcode.com/problems/search-in-rotated-sorted-array

    Algorithm: Binary Search

    This problem is essentially the additional problem in context of Find Minimum in Rotated Sorted Array.
    Just find the index of the minimum element. The subarray before the index of the minimum element is sorted
    Also, the subarray from the minimum element index is also sorted.

    Just apply normal binary search to both subarrays separately to find the element in the rotated sorted array

    Time complexity: O(log n)
    Space complexity: O(1)
    """
    def search(self, nums: List[int], target: int) -> int: # noqa
        min_element_index = find_min_element_index(nums)
        first_part = binary_search(nums, 0, min_element_index - 1, target)
        second_part = binary_search(nums, min_element_index, len(nums) - 1, target)

        return first_part if first_part != -1 else second_part


def find_min_element_index(nums: List[int]) -> int:

    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[left] < nums[right]:
            return left

        mid = left + (right - left) // 2

        if nums[left] <= nums[mid]:
            left = mid + 1
        else:
            right = mid

    return left


def binary_search(nums: List[int], left: int, right: int, target: int) -> int:
    if not nums:
        return -1
    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left if nums[left] == target else -1
