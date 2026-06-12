# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(root,max_v,min_v):
            if not root:
                return True
            print(root.val,max_v,min_v)
            if min_v<root.val and max_v>root.val:
                l = dfs(root.left,root.val,min_v)
                r = dfs(root.right,max_v,root.val)
                return l and r
            else:
                return False
        return dfs(root,float('inf'),-float('inf'))
        
#  2
# 1 3


        