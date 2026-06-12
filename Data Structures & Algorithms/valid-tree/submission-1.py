class UnionFind:
    def __init__(self,n):
        self.par=[i for i in range(n)]
        self.rank=[0]*n
    def find(self,x):
        if self.par[x]==x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    def merge(self,x,y):
        rx = self.find(x)
        ry = self.find(y)
        if rx==ry:
            return False
        if self.rank[rx]<self.rank[ry]:
            rx,ry = ry,rx
        self.par[ry] = rx
        if self.rank[rx]==self.rank[ry]:
            self.rank[rx]+=1
        return True
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        tree = UnionFind(n)
        for a,b in edges:
            ans = tree.merge(a,b)
            if not ans:
                return False
        ans = set()
        for i in range(n):
            ans.add(tree.find(i))
        return True if len(list(ans))==1 else False

# 0
# 1 2 3 
# 4

# 0
# 1 
# 3 2 4
#