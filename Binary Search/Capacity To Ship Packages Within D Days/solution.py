from typing import List


class Solution:
    """
    Problem link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days

    Explanation Link: https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/solutions/769698/python-clear-explanation-powerful-ultimate-binary-search-template-solved-many-problems/ # noqa

    Explanation:
    Binary search probably would not come to our mind when we first meet this problem.
    We might automatically treat weights as search space and then realize we've entered a dead end after wasting
    lots of time. In fact, we are looking for the minimal one among all feasible capacities.

    We dig out the monotonicity of this problem: if we can successfully ship all packages within D days with capacity m,
    then we can definitely ship them all with any capacity larger than m. Now we can design a condition function,
    let's call it feasible, given an input capacity, it returns whether it's possible to ship all packages within D days
    . This can run in a greedy way: if there's still room for the current package, we put this package onto the conveyor
    belt, otherwise we wait for the next day to place this package. If the total days needed exceeds D, we return False,
    otherwise we return True.

    Time Complexity: O(n * sum(weights)), n is the length of the weight array
    Space Complexity: O(1)
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:  # noqa

        def condition(least_weight):
            running_weight = 0
            number_of_days = 1
            for weight in weights:
                running_weight += weight
                if running_weight > least_weight:
                    number_of_days += 1
                    running_weight = weight
            return number_of_days <= days

        """
        Initialize boundary correctly:
        - Obviously capacity should be at least max(weights), otherwise the conveyor belt couldn't ship the heaviest
          package.
        - On the other hand, capacity need not be more than sum(weights), because then we can ship all packages in just
          one day.
        """
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        return left
