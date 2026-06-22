class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def search(nums):
            n = len(nums)
            dp = [0]*n
            dp[0]= nums[0]
            if n==1:
                return dp[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,n):
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
            return dp[-1]
        if len(nums)==1:
            return nums[0]
        return max(search(nums[1:]),search(nums[:-1]))

# 1,1,4,4