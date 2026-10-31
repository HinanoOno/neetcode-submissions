class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        data = [[] for i in range(n)]
        for i in range(n-1):
            data[i].append(i+1)
        dist = list(range(n))
        res = []
        for s,e in queries:
            data[s].append(e)
            if dist[s]+1>=dist[e]:
                res.append(dist[n-1])
                continue
            dist[e] = min(dist[e],dist[s]+1)
            q = deque([])
            q.append(e)
            while q:
                node = q.popleft()
                for nex in data[node]:
                    new_dist = dist[node] + 1
                    if new_dist < dist[nex]:
                        dist[nex] = new_dist
                        q.append(nex)
            res.append(dist[n-1])
        return res
        