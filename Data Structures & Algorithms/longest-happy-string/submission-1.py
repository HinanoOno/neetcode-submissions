class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        data  = []
        ans  =[""]*(a+b+c)
        if a:
            heapq.heappush(data,(-a,"a"))
        if b:
            heapq.heappush(data,(-b,"b"))
        if c:
            heapq.heappush(data,(-c,"c"))
        prev = None
        q = deque([])
        cur =0
        while data:
                cur += 1
                count,val = heapq.heappop(data)
                ans[cur-1]=val
                
                if -count-1>0:
                    if prev==val:
                        q.append((cur+1,val,count+1))
                    else:
                        heapq.heappush(data,(count+1,val))
                prev = val
                if q and q[0][0] == cur:
                    time,val,count =q.popleft()
                    heapq.heappush(data,(count,val))
                
                print(data,cur,q,prev,val)
        return "".join(ans)
# [(-4,c),(-1,b)]
# -4 (4,c,-3)
#  cur=2

