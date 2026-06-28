class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid),len(grid[0])
        INF =2147483647
        q = deque([])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:

                    q.append((i,j,0))
        while q:
            i,j,cnt = q.popleft()
            grid[i][j] = cnt
            for nx,ny in [(1,0),(-1,0),(0,1),(0,-1)]:
                rx,ry = i+nx,j+ny
                if 0<=rx<n and 0<=ry<m and grid[rx][ry] ==INF:
                    grid[rx][ry] = -1
                    q.append((rx,ry,cnt+1))

        