from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int: # noqa
        i = j = answer = 0
        running_multiplication = 1
        while j < len(nums):
            running_multiplication *= nums[j]

            while i < len(nums) and running_multiplication >= k:
                running_multiplication //= nums[i]
                i += 1

            if running_multiplication < k:
                answer += (j - i + 1)

            j += 1

        return answer
