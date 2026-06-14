class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_v,max_v= nums[0],nums[0]
        ans = nums[0]
        for i in range(1,n):
            tmp = min_v
            min_v = min(min_v*nums[i],nums[i],max_v*nums[i])
            max_v = max(max_v*nums[i],nums[i],tmp*nums[i])
            ans = max(ans,max_v)
            print(min_v,max_v)
        return ans
#  [2,4,-3,5]
# min_v = 2, max_v = 2
#  min 4 max 8
# -12 -3 -24 min