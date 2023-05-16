from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in range(len(asteroids)):
            asteroid = asteroids[i]
            while stack and stack[-1] > 0 and asteroid < 0:
                if stack[-1] == abs(asteroid):
                    stack.pop()
                    break
                elif stack[-1] < abs(asteroid):
                    stack.pop()
                    continue
                elif stack[-1] > abs(asteroid):
                    break
            else:
                stack.append(asteroid)
        return stack
