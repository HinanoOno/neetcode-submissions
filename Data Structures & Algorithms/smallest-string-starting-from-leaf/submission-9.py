# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
sys.setrecursionlimit(10000)

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        def dfs(root):
            if not root:
                return None
            cur = chr(root.val+ord("a"))
            #print(root.val)
            l = dfs(root.left)
            r = dfs(root.right)
            if l is None and r is None:
                return cur
            elif r is None:
                return l+cur
            elif l is None:
                return r+cur
            return min(l+cur,r+cur)
        return dfs(root)
        