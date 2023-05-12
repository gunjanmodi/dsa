from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]: # noqa
        first_occurrence = search_first_occurrence(nums, target)
        last_occurrence = search_last_occurrence(nums, target)
        return [first_occurrence, last_occurrence]


def search_first_occurrence(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    first_occurrence = -1
    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            first_occurrence = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return first_occurrence


def search_last_occurrence(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    last_occurrence = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            last_occurrence = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return last_occurrence
