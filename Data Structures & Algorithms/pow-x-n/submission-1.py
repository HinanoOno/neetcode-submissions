class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x==0:
            return 0
        def cur(x,i):
            if i==0:
                return 1
            elif i==1:
                return x
            tmp = cur(x,i//2)
            if i%2==0:
                ans = tmp**2
            else:
                ans = tmp**2*x
            print(ans,x,i)
            return ans
        if n<0:
            n=-n
            return 1/cur(x,n)
        return cur(x,n)
            

# 10-> (2**5)**2
# (1.21)**2*2
# (2)**2