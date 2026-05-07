class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        if len(nums) == 0 or len(nums) == 1:
            return nums
        n = len(nums)
        maxPrefix = [0]*n
        minSuffix = [0]*n
        maxPrefix[0] = nums[0]
        minSuffix[n-1] = nums[n-1]
        for i in range(1, n):
            maxPrefix[i] = max(nums[i], maxPrefix[i-1])
        for j in range(n-2, -1, -1):
            minSuffix[j] = min(nums[j], minSuffix[j+1])
        ans = [0]*n
        ans[n-1] = maxPrefix[n-1]
        for k in range(n-2, -1, -1):
            if maxPrefix[k] > minSuffix[k+1]:
                ans[k] = ans[k+1]
            else:
                ans[k] = maxPrefix[k]
        return ans