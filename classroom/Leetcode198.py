# Top-Down Approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = dict()
        ans = 0

        def f(nums, ind):
            if ind >= len(nums):
                return 0
            if ind in dp:
                return dp[ind]
            skip = f(nums, ind + 1)
            take = nums[ind] + f(nums, ind + 2)
            dp[ind] = max(skip, take)
            return max(skip, take)

        return f(nums, 0)


# Bottom-Up Approach
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        ans = [0]*len(nums)
        ans[0] = nums[0]
        ans[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            ans[i] = max(ans[i-1], nums[i] + ans[i-2])
        return ans[len(nums)-1]