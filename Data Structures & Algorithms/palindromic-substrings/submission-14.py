class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n) for i in range(n)]
        for i in range(n):
            dp[i][i] = 1

        for i in range(n-1,-1,-1):
            for j in range(i,n):
                if i==j:
                    continue
                elif s[i] == s[j]:
                    if j==i+1:
                        dp[i][j] += 1
                    else:
                        dp[i][j] += dp[i+1][j-1]
            #print(dp)
        return sum([sum(i) for i in dp])


        