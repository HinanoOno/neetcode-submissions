class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        n= int(bin(n)[2:])
  
        while n>0:
            ans = n%10
            if ans:
                cnt+=1
            n//=10
        return cnt