# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(root):
            nonlocal res
            if not root:
                res.append("N")
                return
            res.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        print(res)
        ans = ",".join(res)
        return ans

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        n = len(data)
        split = data.split(",")
        print(split)
        cur = 0
        def dfs():
            nonlocal cur,split
            print(cur)
            if split[cur] == "N":
                cur += 1
                return None
            node = TreeNode(split[cur])
            cur += 1
            l = dfs()
            r = dfs()
            node.left = l
            node.right = r
        
            return node
        return dfs()

