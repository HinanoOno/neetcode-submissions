class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        def dfs(i,cur):
            nonlocal ans
            if i==n:
                if cur==target:
                    ans += 1
                return 
            dfs(i+1,cur+nums[i])
            dfs(i+1,cur-nums[i])
        dfs(0,0)
        return ans
        