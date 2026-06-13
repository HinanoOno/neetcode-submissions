# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # pre top->left->right
        # inorder left->top->right

        n = len(preorder)
        cur = 0
        def dfs(inorder):
            nonlocal cur,preorder
            if not inorder:
                return None
            if cur==n:
                return None
            node = TreeNode(preorder[cur])
            cur += 1
            idx = inorder.index(node.val)
            l = dfs(inorder[:idx])
            r = dfs(inorder[idx+1:])
            node.left = l
            node.right = r
            return node
        return dfs(inorder)
# dfs(0) node =1
# dfs([2]) dfs(1,[3,4]) cur = 1
# dfs (1,[3,4]) cur = 2node =3 index= 0
# dfs([4]) 

