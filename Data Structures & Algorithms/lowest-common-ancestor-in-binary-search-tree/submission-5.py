# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def dfs(root,p,q):
            
            if not root:
                return
            print(root.val,q.val,p.val)
            if p.val<=root.val<=q.val:
                return root
            elif p.val<root.val and q.val<root.val:
                return dfs(root.left,p,q)
            elif p.val>root.val and q.val>root.val:
                return dfs(root.right,p,q)
            return root

            
        return dfs(root,p,q)

# l=o r=o node
# l=o r=x node=o => node