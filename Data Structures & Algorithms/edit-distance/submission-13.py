class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        
        # dp[j] は word1の現在の行まで見た時の、word2の j 文字目までの編集距離
        dp = list(range(m + 1))
        
        for i in range(1, n + 1):
            new_dp = [0] * (m + 1)
            new_dp[0] = i # 初期化：空文字との距離
            for j in range(1, m + 1):
                if word1[i-1] == word2[j-1]:
                    new_dp[j] = dp[j-1]
                else:
                    new_dp[j] = 1 + min(dp[j],      # 削除
                                        new_dp[j-1], # 挿入
                                        dp[j-1])    # 置換
            dp = new_dp
            
        return dp[m]