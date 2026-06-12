class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        data = [[]for i in range(n)]
        for a, b in edges:
            data[a].append(b)
            data[b].append(a)
        seen = set()
        res = []
        def dfs(i):
            nonlocal res
            q = deque([i])
            seen.add(i)
            ans = []
            ans.append(i)
            while q:
                node = q.popleft()
                for nex in data[node]:
                    if nex not in seen:
                        seen.add(nex)
                        q.append(nex)
            res.append(ans)
        for i in range(n):
            if i not in seen:
                dfs(i)
        print(res)
        return len(res)
            

        

        