class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        intervals.sort(key=lambda x:[x[1],-x[0]])
        stack = []
        ans = 0
        print(intervals)
    # [1,2][1,4][2,5]
        for i in range(n):
            s,e = intervals[i]
            if stack and stack[-1][1]>s:
                ans += 1
                continue
            stack.append([s,e])
        return ans
        