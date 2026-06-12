class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)
        half = total/2
        
        def dfs(cur,i):
            if cur==half:
                return True
            if i>=n:
                return False
            return dfs(cur+nums[i],i+1) or dfs(cur,i+1)
        return dfs(0,0)