# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
sys.setrecursionlimit(10000)
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        tmp = root
        def dfs(root):
            if not root:
                return "N"
            l = dfs(root.left)
            r = dfs(root.right)
            return str(root.val)+","+l+","+r
        ans = dfs(tmp)
        print(ans)
        return ans

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None

        values = data.split(",")
        self.i = 0

        def dfs():
            if values[self.i]=="N":
                self.i+=1
                return None
            node = TreeNode(int(values[self.i]))
            self.i += 1

            node.left = dfs()
            node.right = dfs()

            return node
        return dfs()
