from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        frequency = [0, 0]
        i = 0
        answer = 0
        for j in range(len(nums)):
            frequency[nums[j]] += 1
            while frequency[0] > k and i <= j:
                frequency[nums[i]] -= 1
                i += 1
            answer = max(answer, j - i + 1)
        return answer