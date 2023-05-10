from typing import List


class Solution:
    """
    Category: Variable size sliding window

    Problem Link: https://leetcode.com/problems/fruit-into-baskets/description/

    This is essentially the same as Longest substring with at most K distinct characters,
    but it is subarrays with at most 2 distinct numbers.

    Complexity Analysis:
        Time Complexity: O(n)
        Space Complexity: O(n)
    """
    def totalFruit(self, fruits: List[int]) -> int: # noqa
        d = dict()
        answer = 0
        i = 0
        for j in range(len(fruits)):
            d[fruits[j]] = d.get(fruits[j], 0) + 1

            if len(d) > 2:
                d[fruits[i]] -= 1
                if d[fruits[i]] == 0:
                    del d[fruits[i]]
                i += 1
            answer = max(answer, j - i + 1)
        return answer
