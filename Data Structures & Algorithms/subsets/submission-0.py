class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        def dfs(cur,nums):
            ans.append(cur[:])
            if len(cur)==n:
                return 
            for i in range(len(nums)):
                cur.append(nums[i])
                dfs(cur,nums[i+1:])
                cur.pop()
        dfs([],nums)
        return ans