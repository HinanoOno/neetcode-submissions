import bisect
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        stack = []

        for i in range(n):
            if stack and temperatures[stack[-1]]<temperatures[i]:
                while stack and temperatures[stack[-1]]<temperatures[i]:
                    res[stack[-1]] = i-stack[-1]
                    stack.pop()

            stack.append(i)
        return res
# [30,38,30,36,35,40,28]
# [0,]
