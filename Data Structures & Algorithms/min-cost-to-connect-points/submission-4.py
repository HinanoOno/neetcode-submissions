class Solution:
    class UnionFind:
        def __init__(self,n):
            self.size = [1]*n
            self.rank = [1]*n
            self.parent = [-1]*n
        def find(self,x):
            if self.parent[x]==-1:
                return x
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

        def is_same(self,x,y):
            return self.find(x)==self.find(y)
        def merge(self,x,y):
            rx,ry = self.find(x),self.find(y)
            if rx == ry:
                return False
            if self.rank[rx]<self.rank[ry]:
                rx,ry = ry,rx
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]
            if self.rank[rx] == self.rank[ry]:
                self.rank[rx]+=1
            return True
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        def calc(x,y):
            return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
        data = []
        for i in range(n):
            for j in range(n):
                if (i==j): continue
                tmp = calc(points[j],points[i])
                data.append((tmp,i,j))
        total,cnt = 0,0
        uf = self.UnionFind(n)
        data.sort()
        for time,a,b in data:
            if uf.merge(a,b):
                total += time
                cnt += 1
                print(total,cnt,a,b)
                if cnt==n-1:
                    break
        return -1 if cnt!=n-1 else total
                

        
        