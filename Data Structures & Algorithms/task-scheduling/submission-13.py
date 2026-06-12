class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = len(tasks)
        cnt = Counter(tasks)
        q = []
        for i,v in cnt.items():
            heapq.heappush(q,(-v,i))
        time = 0
        data = deque([])
        while q or data:
            time += 1
            if not q:
                time = data[0][1]
            else:
                val,node = heapq.heappop(q)
                if (-val-1)>0:
                    data.append([val+1,time+n,node])
            if data and data[0][1] == time:
                heapq.heappush(q,(data[0][0],data[0][2]))
                data.popleft()
            print(data,q,time)
        return time
            
                
#(max_freq-1)*(n+1) + max_freq_count
# (2-1)*2 + 2 = 5
# (2)*4 +1 - 9

