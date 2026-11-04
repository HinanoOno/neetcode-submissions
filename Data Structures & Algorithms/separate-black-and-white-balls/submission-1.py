class Solution:
    def minimumSteps(self, s: str) -> int:
        n = len(s)
        l = 0
        cnt =0 
        for i in range(n):
            if s[i]=="0":
                cnt+=(i-l)
                l+=1
            #print(data)
        return cnt
