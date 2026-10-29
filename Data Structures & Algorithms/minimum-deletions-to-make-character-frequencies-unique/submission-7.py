import bisect
class Solution:
    def minDeletions(self, s: str) -> int:
        cnt = Counter(s)
        n = len(s)
        ans = 0
        data = [0]*(n+1)
        for i,v in cnt.items():
            data[v]+=1
        ans = 0
        for i in range(n-1,0,-1):
            if data[i]>1:
                data[i-1]+=data[i]-1
                ans += data[i]-1
                data[i] = 1
        return ans
