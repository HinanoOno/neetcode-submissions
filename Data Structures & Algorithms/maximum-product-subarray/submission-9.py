class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        ans = -float('inf')
        for i in range(n):
            cur = nums[i]
            ans = max(ans,cur)
            for j in range(i+1,n):
                cur*=nums[j]
                ans = max(ans,cur)
        return ans 
       
            
# nums =  [2,4,-3,-5]
# cur = 1
# cur = 8
# max_V=8 min_v = -24
# max_v= 1 


# [-3,0,-2]
# cur = 1
# -3<0:
# cur = 0
# 0