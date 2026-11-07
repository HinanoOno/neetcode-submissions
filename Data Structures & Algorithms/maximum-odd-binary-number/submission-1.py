class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        s = [c for c in s]
        left = 0
        n = len(s)
        
        for i in range(n):
            if s[i]=="1":
                s[i],s[left] = s[left],s[i]
                left+=1
        print(s)
        s[left-1],s[-1] = s[-1],s[left-1]
        return "".join(s)
    # 1100    