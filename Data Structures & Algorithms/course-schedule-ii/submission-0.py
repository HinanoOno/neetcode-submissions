class Solution:
    def findOrder(self, n: int, prerequisites: List[List[int]]) -> List[int]:
        data = [[] for i in range(n)]   
        deg = [0]*n
        q = deque([])
        ans = []
        for a,b in prerequisites:
            data[b].append(a)
            deg[a]+=1
        for i in range(n):
            if deg[i]==0:
                q.append(i)
        while q:
            node = q.popleft()
            ans.append(node)
            for nex in data[node]:
                deg[nex]-=1
                if deg[nex]==0:
                    q.append(nex)
        
        for i in range(n):
            if deg[i]!=0:
                return []
        return ans
