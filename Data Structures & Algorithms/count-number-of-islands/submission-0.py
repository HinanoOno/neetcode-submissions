class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n,m = len(grid),len(grid[0])
        ans = 0
        def dfs(i,j):
        
            for ni,nj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ri,rj = i+ni,j+nj
                if 0<=ri<n and 0<=rj<m and grid[ri][rj] =="1":
                    grid[ri][rj] = "0"
                    dfs(ri,rj)
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    grid[i][j] ="0"
                    dfs(i,j)
                    ans += 1
                    print(grid)
        return ans

        
            
        