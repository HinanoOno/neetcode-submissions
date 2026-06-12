# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        data = defaultdict(int)
        if not root:
            return 0
        res = -float('inf')
        def dfs(cur):
            nonlocal res
            if not cur:
                return 0
            if cur.left:
                l = dfs(cur.left)
            else:
                l = 0
            if cur.right:
                r = dfs (cur.right)
            else:
                r = 0
            ans = max(max(l,0),max(r,0)) + cur.val
            res = max(res,max(l,0)+max(r,0)+cur.val)
            return ans
        dfs(root)
        return res
    
# dfs(10) 
# l=0 r= 0 ans = 10
# l= 10 dfs(20) 35
# l= dfs(15) 15
# l= dfs(-5) ans = -5
# r = 5 ans = 5