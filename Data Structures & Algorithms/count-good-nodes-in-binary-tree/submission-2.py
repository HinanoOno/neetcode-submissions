# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans =0
        
        def dfs(root,max_v):
            nonlocal ans
            if not root:
                return 
            print(root.val,max_v)
            if root.val>=max_v:
                ans +=1
                max_v = root.val
            dfs(root.left,max_v)
            dfs(root.right,max_v)

        dfs(root,-float('inf'))
        return ans
           
# 2 max2
# 1
# 3 