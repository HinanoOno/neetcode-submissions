class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        sell_dp = [0]*(n+1)
        buy_dp = [0]*(n+1)
        buy_dp[1] = -prices[0]

        for i in range(2,n+1):
            buy_dp[i] = max(sell_dp[i-2]-prices[i-1],buy_dp[i-1])
            sell_dp[i] = max(buy_dp[i-1]+prices[i-1],sell_dp[i-1])

        return max(buy_dp[-1],sell_dp[-1])


        