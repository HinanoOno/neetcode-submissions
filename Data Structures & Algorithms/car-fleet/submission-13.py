class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        ans = n
        dp = [0]*n
        data = []
        
        for i in range(n):
            dp[i] = (target-position[i])/speed[i]
            data.append((position[i],dp[i]))
  
        data.sort(key = lambda x:x[0],reverse = True)
        max_v = 0
        for i in range(n):
            arrive = data[i][1]
            if arrive>max_v:
                max_v = arrive
            elif arrive<=max_v:
                ans -= 1
        return ans


