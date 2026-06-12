class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        n = len(intervals)
        m = len(queries)
        ans = []

        for i in range(m):
            cur = []
            query = queries[i]
            for j in range(n):
                s,e = intervals[j]
      
                if  s<=query<=e:
                    cur.append([s,e,j])

            cur.sort(key=lambda x: x[1]-x[0])
            if cur:
                ans.append(cur[0][1]-cur[0][0]+1)
            else:
                ans.append(-1)
        return ans

        