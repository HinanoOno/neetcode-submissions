class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank = [0]*n
    def find(self,x):
        if self.par[x]==x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def merge(self,x,y):
        if self.find(x)==self.find(y):
            return False
        rx,ry =self.par[x],self.par[y]
        if self.rank[rx]<self.rank[ry]:
            rx,ry = ry,rx
        self.par[ry] = rx
        if self.rank[rx]==self.rank[ry]:
            self.rank[rx]+=1
        return True
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        tree = UnionFind(n)
        seen = set()
        cnt = n
        for a,b in edges:
            if tree.merge(a,b):
                cnt -= 1
        return cnt