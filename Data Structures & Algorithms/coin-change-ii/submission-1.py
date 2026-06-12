class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [0]*(amount+1)
        dp[0] = 1

        
        for j in range(n):
            for  i in range(1,amount+1):
                if (i-coins[j])>=0 and dp[i-coins[j]]:
                    dp[i] += dp[i-coins[j]]
        return dp[amount]

        