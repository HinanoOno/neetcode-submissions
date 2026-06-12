"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)
        n = len(intervals)
        if n==0:
            return n
        rooms = []
        ans = 1
        heapq.heappush(rooms,intervals[0].end)

        for i in range(1,n):
            while rooms and rooms[0]<=intervals[i].start:
                heapq.heappop(rooms)
            heapq.heappush(rooms,intervals[i].end)
            ans = max(ans,len(rooms))
        return ans