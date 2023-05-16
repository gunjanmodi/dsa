from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int: # noqa
        position_idx, speed_idx = 0, 1
        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars.sort(key=lambda x: x[position_idx], reverse=True)
        stack = []
        for i in range(len(cars)):
            factor = (target - cars[i][position_idx]) / cars[i][speed_idx]
            if not stack:
                stack.append(factor)
            elif factor > stack[-1]:
                stack.append(factor)
        return len(stack)
