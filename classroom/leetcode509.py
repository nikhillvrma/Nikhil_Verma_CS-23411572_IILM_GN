# Recursive Approach

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


# Dynamic Programming Approach

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        mp = [0] * (n + 1)
        mp[0] = 0
        mp[1] = 1
        for i in range(2, n + 1):
            mp[i] = mp[i - 1] + mp[i - 2]
        return mp[n]
