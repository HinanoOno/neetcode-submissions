class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)

        def check(mid):
            ans = 0
            for i in range(n):
                ans += math.ceil(piles[i]/mid) if piles[i]>=mid else 1
            print(ans,mid)
            return True if ans<=h else False
        
        l,r = 1,max(piles)
        while l<r:
            mid = (l+r)//2
            if check(mid):
                r= mid
            else:
                l=mid+1
        return r


"[15,10,23,4]"
# l= 0 r=23 mid = 11
# l=12 r=23 mid =18


# [1,4,3,2] h=9
# l=0 r=4 mid = 2
# 1,2,2,1, => 6
# mid = 1 10
