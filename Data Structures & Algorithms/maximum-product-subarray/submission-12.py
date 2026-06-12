class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_v = nums[0]
        cur_v= nums[0]
        cur_min = nums[0]
        for i in range(1,n):
            tmp1 = cur_v
            tmp2 =cur_min
            cur_v = max(nums[i],cur_v*nums[i],cur_min*nums[i])
            cur_min = min(nums[i],tmp1*nums[i],tmp2*nums[i])
            max_v = max(max_v,cur_v)
        return max_v
            
            
# nums =  [-4,-3,-2]
# -4,-4,-24  cur_v=12,cur_min=-3 max=12