class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        q = deque([])
        ans = 0
        seen = set()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                    seen.add((i,j))
        while q:
            x,y,cnt = q.popleft() #(2,2,0)
            print(x,y,cnt)
            ans = max(ans,cnt)
            for nx,ny in[(0,1),(0,-1),(1,0),(-1,0)]:
                rx,ry = x+nx,y+ny
                if 0<=rx<n and 0<=ry<m and grid[rx][ry]==1:
                    grid[rx][ry] = 2

                    q.append((rx,ry,cnt+1))
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    return -1
        return ans

#[1,0,1]
#[0,2,0]
#[1,0,1]
#1s-4s = max distanc from rotate cell to1 cell