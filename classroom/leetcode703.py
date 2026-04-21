import heapq as h


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        h.heapify(self.nums)
        while len(self.nums) > k:
            h.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            h.heappush(self.nums, val)
        elif val > self.nums[0]:
            h.heapreplace(self.nums, val)

        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
