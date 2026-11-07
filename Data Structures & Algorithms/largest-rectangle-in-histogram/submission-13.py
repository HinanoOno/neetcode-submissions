class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        s = []

        ans = 0
        for i in range(n+1):

            while s and (i==n or heights[s[-1]]>=heights[i]):
                    pre = heights[s.pop()]
                    last = -1 if not s else s[-1]
                    if last==-1:
                        ans = max(ans,pre*(i))
                    else:   
                        ans = max(ans,pre*(i-last-1))
            s.append(i)
        return ans
# [1,2,4] ans =7,7,4