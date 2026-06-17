class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ans = float('inf')
        memo = {}

        def dfs(cur,i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i==0 and j==0:
                return 1
            top,left = 0,0
            if (i-1)>=0:
                left = dfs(cur,i-1,j)
            if (j-1)>=0:
                top = dfs(cur,i,j-1)
            memo[(i,j)] = top+left
            return top+left
        return dfs(0,n-1,m-1)
            
# (2,5) (1,5) (2,4)    (0,5) (1,4) 