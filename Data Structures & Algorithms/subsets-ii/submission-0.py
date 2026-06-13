class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()
        nums.sort()
        def dfs(i,cur):
            if i==n:
                ans.add(tuple(cur))
                return 
            dfs(i+1,cur+[nums[i]])
            dfs(i+1,cur)
        
        dfs(0,[])
        return list(ans)
# nums = [1,2,1]
# [] dfs([],0)
# dfs([1],1) [1,2,1]
# dfs(2) [1,2]
# dfs(3) [1,2,1]
# dfs(2)[1,1]
# dfs(3) [1,1,2]
# dfs