class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [float('-inf')]*(n+1)
        dp[n] = 0
    # dp[i] = 現在のプレイヤーの得点-相手の得点の最大値
        for i in range(n-1,-1,-1):
            cnt = 0
            for j in range(i,min(n,i+3)):
                cnt += stoneValue[j]
                dp[i] = max(dp[i],cnt-dp[j+1])
        print(dp)
        result = dp[0]
        if result == 0:
            return "Tie"
        return "Alice" if result > 0 else "Bob"


