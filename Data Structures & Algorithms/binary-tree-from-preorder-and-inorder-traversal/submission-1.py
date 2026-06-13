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
        indices = {val:idx for idx,val in enumerate(inorder)}
        print(indices)
        n = len(preorder)
        cur = 0
        def dfs(l,r):
            nonlocal cur
            if l>r:
                return None
            root_val = preorder[cur]
            cur += 1
            root = TreeNode(root_val)
            mid = indices[root_val]
            l = dfs(l,mid-1)
            r = dfs(mid+1,r)
            root.left = l
            root.right =r
            return root
        return dfs(0,n-1)
# dfs(0) node =1
# dfs([2]) dfs(1,[3,4]) cur = 1
# dfs (1,[3,4]) cur = 2node =3 index= 0
# dfs([4]) 

