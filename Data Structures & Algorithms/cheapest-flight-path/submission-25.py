class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        data = [[] for i in range(n)]
        for a,b,cost in flights:
            data[a].append((b,cost))
        
        costs = [float('inf')]*n

        q = deque([])
        q.append((0,0,src))
        costs[src]=0
        cur = 0
        while q:
            for i in range(len(q)):
                total,cur,spot = q.popleft()
                if total>k:
                    continue
   
                for nex,cost in data[spot]:
                    if costs[nex]>cur+cost:
                        costs[nex] = cur+cost
                        q.append((total+1,costs[nex],nex))

        print(costs)
        return costs[dst] if costs[dst]!=float('inf') else -1
# [[(1,200)],[(0,200),(3,300)],[(1,100)]]

    