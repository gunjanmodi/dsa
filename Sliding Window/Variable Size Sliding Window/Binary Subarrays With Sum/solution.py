from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:  # noqa
        """
        Algorithm: Sliding Window
        Pattern: Variable size sliding window


        at_most_subarray_sum actually calculates the number of subarrays which is having sum less than
        and equal to goal. Now the catch is this function will return the number of subarrays
        having sum less than goal too.

        Hence to remove the calculation of less or equal we call the same function again for goal - 1.
        Why?
        at_most_subarray_sum(nums,goal) will give you number of subarrays with sum <= goal
          i.e. goal, goal-1 , goal-2 , goal-3 ... 0

        at_most_subarray_sum(nums,goal) will give you number of subarrays with sum <= goal -1
         i.e. goal-1 , goal-2 , goal-3 ... 0
        So we subtract both.


        Time Complexity: O(n)
        Space Complexity: O(1)

        """

        def at_most_subarray_sum(_nums, _goal):
            running_sum = answer = 0
            i = 0
            for j in range(len(_nums)):
                running_sum += nums[j]

                while i <= j and running_sum > _goal:
                    running_sum -= nums[i]
                    i += 1

                answer += (j - i + 1)

            return answer

        return at_most_subarray_sum(nums, goal) - at_most_subarray_sum(nums, goal - 1)



