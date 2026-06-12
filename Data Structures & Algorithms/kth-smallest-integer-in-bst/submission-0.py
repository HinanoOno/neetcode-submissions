# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        cur = []
        def dfs(root):
            if not root:
                return 
            heapq.heappush(cur,root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        while k>0:
            num = heapq.heappop(cur)
            k-=1
            if k==0:
                return num
            

            
        