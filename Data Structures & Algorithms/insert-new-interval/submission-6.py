class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        n = len(intervals)
        stack = [intervals[0]]

        for s,e in intervals[1:]:
            if s>stack[-1][1]:
                stack.append([s,e])
            else:
            
                stack[-1] = [min(stack[-1][0],s),max(stack[-1][1],e)]
        return stack

        