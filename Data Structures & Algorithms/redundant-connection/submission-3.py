class UnionFind:
    def __init__(self,n):
        self.size = [1]*n
        self.par = [i for i in range(n)]
        self.rank = [0]*n
    def find(self,x):
        if self.par[x]==x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]
    def is_same(self,x,y):
        rx,ry =self.par[x],self.par[y]
        return self.find(rx) ==self.find(ry)
    def merge(self,x,y):
        rx,ry =self.par[x],self.par[y]
        if rx==ry:
            return False
        if self.rank[rx]<self.rank[ry]:
            rx,ry = ry,rx
        self.par[ry] =rx
        self.size[rx]+=self.size[ry]
        if self.rank[rx]==self.rank[ry]:
            self.rank[rx]+=1
        return True
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        tree = UnionFind(n)
        for a,b in edges:
            if tree.is_same(a-1,b-1):
                return [a,b]
            tree.merge(a-1,b-1)
            print(tree.par)
        return [-1,-1]

        
        