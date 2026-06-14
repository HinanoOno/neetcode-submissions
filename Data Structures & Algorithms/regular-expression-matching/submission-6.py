class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s),len(p)
        dp = [[False]*(n+1) for i in range(m+1)]
        dp[0][0] = True

        for j in range(2, m + 1):
            if p[j-1] == '*':
                dp[j][0] = dp[j-2][0]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[j-1]==p[i-1] or p[i-1]==".":
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1]=="*":
                    dp[i][j] = dp[i-2][j]
                    if p[i-2]=="." or p[i-2] == s[j-1]:
                        dp[i][j] = dp[i][j] or dp[i][j-1]
            print(dp)
        return dp[-1][-1]

