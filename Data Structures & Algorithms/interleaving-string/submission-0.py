class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a,b = len(s1),len(s2)
        c = len(s3)
        if a+b != c:
            return False
        dp = [[False]*(b+1) for i in range(a+1)]

        dp[a][b] = True
        for i in range(a,-1,-1):
            for j in range(b,-1,-1):
                if i<a and s1[i] == s3[i+j] and dp[i+1][j]:
                    dp[i][j] = True
                if j<b and s2[j] == s3[i+j] and dp[i][j+1]:
                    dp[i][j] = True
        return dp[0][0]

                
            


        