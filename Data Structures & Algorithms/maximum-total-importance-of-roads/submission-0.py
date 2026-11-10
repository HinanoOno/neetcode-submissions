class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        data = [[] for i in range(n)]
        deg = [0]*n

        for s,e in roads:
            data[s].append(e)
            data[e].append(s)
            deg[s]+=1
            deg[e]+=1
        deg.sort(reverse=True)
        ans = 0
        for i in range(n):
            ans+=deg[i]*n
            n-=1
        return ans
        
        