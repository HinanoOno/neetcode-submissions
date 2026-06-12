class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n= len(candidates)
        ans = []
        candidates.sort()
        def dfs(i,cur,total):
            print(i,cur,total)
            if total==target:
                ans.append(cur[:])
                return 
            for j in range(i,n):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if total+candidates[j]<=target:
                    cur.append(candidates[j])
                    dfs(j+1,cur,total+candidates[j])
                    cur.pop()
        dfs(0,[],0)
        return ans

# candidates = [9,2,2,4,6,1,5], target = 8
# [1,2,2,4,5,6,9]
# dfs(0,[],0)
# dfs(1,[1],1)
# dfs(2,[1,2],3)
# dfs(3,[1,2,2],5)
# dfs(5,[1,2,5],8)
# dfs(3,[1,2])