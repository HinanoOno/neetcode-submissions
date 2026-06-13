class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        l,r = [prices[0]]*n,[prices[-1]]*n
        for i in range(1,n):
            if prices[i]<l[i-1]:
                l[i] = prices[i]
            else:
                l[i] = l[i-1]
        for i in range(n-2,-1,-1):
            if prices[i]>r[i+1]:
                r[i] = prices[i]
            else:
                r[i] = r[i+1]
        max_v=0
        for i in range(n):
            tmp = r[i]-l[i]
            if tmp>max_v:
                max_v = tmp
        return max_v

# [10,1,5,6,7,1]
# [10,1,1,1,1,1]
# [10,7,7,7,7,1]