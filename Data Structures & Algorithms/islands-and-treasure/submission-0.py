class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n,m = len(grid),len(grid[0])
        INF = 2147483647
        ans = grid.copy()
        def bfs(i,j):
            q = deque([])
            q.append((i,j,1))
            seen = set()
            seen.add((i,j))
 
            while q:
                x,y,cur = q.popleft()

                for rx,ry in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny =x+rx,y+ry
                    if 0<=nx<n and 0<=ny<m and grid[nx][ny] not in [0,-1]:
                        if (nx,ny) in seen:
                            continue
                        #rint(nx,ny,"a")
                        q.append((nx,ny,cur+1)) 
                        seen.add((nx,ny))
                        grid[nx][ny] = min(grid[nx][ny],cur)
        for i in range(n):
            for j in range(m):
                if grid[i][j] ==0:
                    bfs(i,j)
     