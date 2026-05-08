from collections import deque, defaultdict
from typing import List

class Solution:

    def isPrime(self, a):
        if a < 2:
            return False
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
        return True

    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        mp = defaultdict(list)
        for i in range(n):
            mp[nums[i]].append(i)
        q = deque()
        q.append((0, 0))
        visited = set()
        visited.add(0)
        usedPrime = set()
        mx = max(nums)
        while q:
            i, jumps = q.popleft()
            if i == n - 1:
                return jumps
            if i + 1 < n and (i + 1) not in visited:
                visited.add(i + 1)
                q.append((i + 1, jumps + 1))
            if i - 1 >= 0 and (i - 1) not in visited:
                visited.add(i - 1)
                q.append((i - 1, jumps + 1))
            if self.isPrime(nums[i]) and nums[i] not in usedPrime:
                val = nums[i]
                multiple = val
                while multiple <= mx:
                    if multiple in mp:
                        for _ in mp[multiple]:
                            if _ not in visited:
                                visited.add(_)
                                q.append((_, jumps + 1))
                    multiple += val
                usedPrime.add(val)
        return -1