class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights+=[0]
        n = len(heights)
        s = []

        ans = 0
        for i in range(n):
            h = heights[i]
            if not s or heights[s[-1]]<h:
                s.append(i)
            else:
                while s and heights[s[-1]]>=h:
                    pre = heights[s.pop()]
                    last = -1 if not s else s[-1]
                    if last==-1:
                        ans = max(ans,pre*(i))
                    else:   
                        ans = max(ans,pre*(i-last-1))
                s.append(i)
        return ans
# [1,2,4] ans =7,7,4