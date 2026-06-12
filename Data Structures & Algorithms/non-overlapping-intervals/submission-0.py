class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key = lambda x :x[1])
        prev = None
        cur = 0
        for s,e in  intervals:
            if prev and prev>s:
                cur += 1
            else:
                prev = e
        return cur

# intervals = [[1,2],[2,4],[1,4]]
# [[1,2],[1,4],[2,4]]
# 