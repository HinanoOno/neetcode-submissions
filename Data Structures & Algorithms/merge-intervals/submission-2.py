class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort()
        ans = [intervals[0]]
        for i in range(1,n):
            s,e = intervals[i]
            if ans[-1][1]>=s:
                ans[-1] = [min(s,ans[-1][0]),max(e,ans[-1][1])]
            else:
                ans.append([s,e])
        return ans


        