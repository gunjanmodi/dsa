from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int: # noqa
        i = j = 0
        total = answer = 0

        nums.sort()

        while j < len(nums):
            total += nums[j]
            if (j - i + 1) * nums[j] - total > k:
                total -= nums[i]
                i += 1
            answer = max(answer, j - i + 1)
            j += 1
        return answer
