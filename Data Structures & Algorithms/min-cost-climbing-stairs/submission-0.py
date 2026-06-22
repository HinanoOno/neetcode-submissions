class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [float('inf')]*(n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            if i>=1:
                dp[i] = min(dp[i],dp[i-1]+cost[i-1])
            if i>=2:
                dp[i] = min(dp[i],dp[i-2]+cost[i-2])
        print(dp)
        return dp[-1]

        
    
# cost[1,2,1,2,1,1,1]
# [0,1,2,2,3,4,4]