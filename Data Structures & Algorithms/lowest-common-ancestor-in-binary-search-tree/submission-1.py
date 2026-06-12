# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def dfs(root,par,p,q):
            if not root:
                return
            if root.val == p.val or root.val ==q.val:
                return root
            left = dfs(root.left,root,p,q)
            right = dfs(root.right,root,p,q)
            #print(left,right,root.val)
            return root if left and right else left or right
        return dfs(root,root,p,q)