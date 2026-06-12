class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        res = 0
        def dfs(i,j,cnt):
            ans =1
            for ri,rj in [(1,0),(0,1),(0,-1),(-1,0)]:
                ni,nj = i+ri,j+rj
                if 0<=ni<n and 0<=nj<m and grid[ni][nj]==1:
                    grid[ni][nj]=-1
                    ans += dfs(ni,nj,cnt+1)
            return ans
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    grid[i][j]=-1
                    res = max(res,dfs(i,j,1))
        return res
        