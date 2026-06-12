class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        cnt = [float('inf')]*n
        data =[[]for i in range(n)]
        for u,v,t in times:
            data[u-1].append((v-1,t))
        cnt[k-1] = 0
        q = [(0,k-1)]
        while q:
            time,node = heapq.heappop(q)
            if time>cnt[node]:
                continue
            for nex,t in data[node]:
                if cnt[nex]>cnt[node]+t:
                    cnt[nex] = cnt[node]+t
                    q.append((cnt[nex],nex))
        ans = 0
        for c in cnt:
            if c==float('inf'):
                return -1
            ans = max(ans,c)
        return ans if ans!=float('inf') else -1