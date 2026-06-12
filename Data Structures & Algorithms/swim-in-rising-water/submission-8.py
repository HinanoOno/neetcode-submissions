
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        ans = float('inf')
        q = []
        
        for ni,nj in [(0,1),(0,-1),(1,0),(-1,0)]:

            if 0<=ni<n and 0<=nj<m:
                heapq.heappush(q,(max(grid[0][0],grid[ni][nj]),ni,nj))
                grid[ni][nj] = -1
        
        while q:
            cur,i,j = heapq.heappop(q)
            #print(cur,i,j)
            if i==n-1 and j==m-1:
                ans = min(ans,cur)
                continue
            for ri,rj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni,nj = ri+i,rj+j
                if 0<=ni<n and 0<=nj<m and grid[ni][nj]!=-1:
                    max_v = max(cur,grid[ni][nj])
                    heapq.heappush(q,(max_v,ni,nj))
                    grid[ni][nj]=-1
        
        return ans if ans!=float('inf') else -1
