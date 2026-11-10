from collections import defaultdict
class UnionFind:
    def __init__(self,n):
        self.par = [i for i in range(n)]
        self.rank = [0]*n
        self.size = [1]*n

    def find(self,x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    def merge(self,x,y):
        rx,ry =self.find(x),self.find(y)
        if rx==ry:
            return False
        if self.rank[ry]>self.rank[rx]:
            rx,ry = ry,rx
        self.par[ry] = rx
        self.size[rx]+=self.size[ry]
        if self.rank[ry]==self.rank[rx]:
            self.rank[rx]+=1
        return True

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n,m = len(grid),len(grid[0])
        uf = UnionFind(n*m)
        def idx(i, j):
            return i * m + j

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    if i + 1 < n and grid[i+1][j] == 1:
                        uf.merge(idx(i, j), idx(i+1, j))

                    if j + 1 < m and grid[i][j+1] == 1:
                        uf.merge(idx(i, j), idx(i, j+1))
        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    seen = set()
                    tmp = 1
                    for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                        nx, ny = i + dx, j + dy

                        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                            root = uf.find(idx(nx, ny))
                            if root not in seen:
                                seen.add(root)
                                tmp += uf.size[root]
                    ans = max(ans,tmp)
        data = defaultdict(int)
        for i in range(n*m):
            data[uf.find(i)]+=1
        return max(ans,max(data.values()))


