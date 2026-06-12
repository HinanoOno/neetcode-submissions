# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0 
        def dfs(root,cur):
            nonlocal ans
            if not root:
                return 
            print(root.val,cur,ans)
            if root.val>=cur:
                    ans += 1
            dfs(root.left,max(cur,root.val))
            dfs(root.right,max(cur,root.val))
        dfs(root,-float('inf'))
        return ans
            
# dfs(2,1) +1
# dfs(3,3) +1
# dfs(3,4) + 1
# dfs(-1,1)
