# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        data = defaultdict(int)
        ans = -float('inf')

        def dfs(cur,root):
            nonlocal ans
            if not root:
                return 
            l = dfs(cur+root.val,root.left)
            r = dfs(cur+root.val,root.right)
            l = max(l,0) if l else 0
            r = max(r,0) if r else 0
            ans = max(ans,l+r+root.val)
            return max(l,r)+root.val
        dfs(0,root)
        return ans

    
#l=-5, r=0
# ans 15
# 15
# 15 # 5