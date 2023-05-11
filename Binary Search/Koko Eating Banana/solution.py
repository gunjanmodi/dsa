from typing import List


class Solution:
    """

    Problem link: https://leetcode.com/problems/koko-eating-bananas/

    Algorithm: Binary Search

    Well detailed explanation:
    https://leetcode.com/problems/koko-eating-bananas/solutions/1703687/java-c-a-very-very-well-detailed-explanation/


    Time Complexity: O(n * log(m)) where n is number of piles, m is range of k (left to right)
    Space Complexity: O(1)
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:  # noqa
        left = 1
        right = 1000000000

        def can_eat_in_time(speed):
            total_hours_taken_with_this_speed = 0

            for pile in piles:
                time_to_eat_this_pile = pile // speed
                total_hours_taken_with_this_speed += time_to_eat_this_pile
                if pile % speed != 0:
                    total_hours_taken_with_this_speed += 1
            return total_hours_taken_with_this_speed <= h

        while left < right:
            mid = left + (right - left) // 2

            if can_eat_in_time(mid):
                right = mid
            else:
                left = mid + 1

        return left
