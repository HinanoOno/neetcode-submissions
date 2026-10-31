class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = deque([])
        for i in range(m):
            if grid[i][0]==1:
                q.append((i,0))
                grid[i][0]=-1
            if grid[i][n-1]==1:
                q.append((i,n-1))
                grid[i][n-1]=-1
        for j in range(n):
            if grid[0][j]==1:
                q.append((0,j))
                grid[0][j] = -1
            if grid[m-1][j]==1:
                q.append((m-1,j))
                grid[m-1][j] = -1
        print(q)
        while q:
            x,y = q.popleft()
            for nx,ny in [(1,0),(-1,0),(0,1),(0,-1)]:
                rx,ry = x+nx,y+ny
                if 0<=rx<m and 0<=ry<n and grid[rx][ry]==1:
                    grid[rx][ry] = -1
                    q.append((rx,ry))

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    ans+=1
        return ans
