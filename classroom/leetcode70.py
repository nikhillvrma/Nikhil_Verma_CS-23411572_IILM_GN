# Recursive Approach
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        x = self.climbStairs(n - 1)
        y = self.climbStairs(n - 2)
        return x + y


# Dynamic Programming Approach
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        mp = [0] * (n + 1)
        mp[0] = 1
        mp[1] = 1
        for i in range(2, n + 1):
            mp[i] = mp[i - 1] + mp[i - 2]
        return mp[n]
