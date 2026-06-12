class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = [float('inf')]*(amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for j in range(n):
                if i-coins[j]>=0:
                    dp[i] = min(dp[i],dp[i-coins[j]]+1)
        print(dp[-1])
        return dp[-1] if dp[-1]!=float('inf') else -1


# [1,2,4] amount = 5
# 10 + 1+ 1 
#[0,1,1,2,1,2]

# [1,2,4,7] amount = 12
# 7 4 1
