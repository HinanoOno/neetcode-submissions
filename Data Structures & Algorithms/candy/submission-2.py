class Solution:
    def candy(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        for i in range(1,n):
            if nums[i]>nums[i-1] and dp[i]<=dp[i-1]:
                dp[i] = dp[i-1]+1
            else:
                dp[i] = 1
        print(dp)
        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1] and dp[i]<=dp[i+1]:
                dp[i] = dp[i+1]+1
            else:
                dp[i]= max(dp[i],1)
        print(dp)
        return sum(dp)
