class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []

        def dfs(cur,data):
            if len(cur)==n:
                ans.append(cur[:])
                return
            for j in range(len(data)):
                dfs(cur+[data[j]],data[:j]+data[j+1:])
        dfs([],nums)
        return ans



# 