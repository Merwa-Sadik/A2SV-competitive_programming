# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        prev1 = 3
        prev2 = 2
        current = 0

        for _ in range(3, n):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        return current