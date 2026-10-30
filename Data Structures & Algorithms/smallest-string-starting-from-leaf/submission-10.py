# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque([])
        ch = chr(root.val+ord("a"))
        q.append((root,ch))
        ans = ""
        while q:
            node,cur = q.popleft()
            if not node.left and not node.right:
                if ans=="":
                    ans = cur
                else:
                    ans = min(ans,cur)
                continue
            if node.left:
                ch = chr(node.left.val+ord("a"))
                q.append((node.left,ch+cur))
            if node.right:
                ch = chr(node.right.val+ord("a"))
                q.append((node.right,ch+cur))
        return ans
        


        