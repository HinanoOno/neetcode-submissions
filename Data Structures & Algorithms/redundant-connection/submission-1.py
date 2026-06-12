class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        data = [[]for i in range(n)]
        for a,b in edges:
            data[a-1].append(b-1)
            data[b-1].append(a-1)
        print(data)
        def bfs(i,data):
            q = deque([])
            q.append(i)
            seen = set()
            seen.add(i)

            while q:
                i = q.popleft()
                for nex in data[i]:
                    if  nex not in seen:
                        q.append(nex)
                        seen.add(nex)
            if len(seen) == len(data):
                return True
            else:
                return False
        for i in range(n-1,-1,-1):
            a,b = edges[i]
            data[a-1].remove(b-1)
            data[b-1].remove(a-1)
            if bfs(i,data):
                return edges[i]
            data[a-1].append(b-1)
            data[b-1].append(a-1)
        return [-1,-1]
        


        