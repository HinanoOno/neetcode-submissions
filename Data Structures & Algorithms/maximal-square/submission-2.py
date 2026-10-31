class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        dp = [[0]*(n+1) for i in range(m+1)]
        dp[0][0] = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if matrix[i-1][j-1]=="0":
                    continue
                else:
                    dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1

        max_v = max([max(a) for a in dp])
        return max_v**2