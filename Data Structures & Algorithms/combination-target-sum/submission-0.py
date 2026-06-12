class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        def dfs(cur,idx,comb):
            nonlocal ans
            if idx==n:
                return 
            if cur==target:
                ans.append(comb)
            elif cur>target:
                return 
            for nex in range(idx,n):
                dfs(cur+nums[nex],nex,comb+[nums[nex]])
        dfs(0,0,[])
        return ans
        
        