# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx= 0
        n = len(preorder)
        data = {}
        for i,v in enumerate(inorder):
            data[v] = i
        def dfs(left,right):
            nonlocal idx
            if left>=right:
                return None
            if idx>=n:
                return None
            node = TreeNode(preorder[idx])
            idx += 1
            index = data[node.val]
            l = dfs(left,index)
            r = dfs(index+1,right)
            node.left,node.right = l,r
            print(node.val)
            return node
        return dfs(0,n)

# [2 34]
# (0,1)
# 0
