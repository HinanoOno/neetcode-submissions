class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        m = len(nums)
        nums = [1]+nums+[1]
        n = len(nums)
        dp = [[0]*n for i in range(n)]
   
        # dp[l][r] = [l,r]の風船をすべて破裂させたときの最大コイン数
        for l in range(n-2,0,-1):
            for r in range(l,n-1):
                for k in range(l,r+1):
                    dp[l][r] = max(dp[l][r],dp[l][k-1]+nums[l-1]*nums[k]*nums[r+1] + dp[k+1][r])
        #print(dp)
        return dp[1][m]
            
        

