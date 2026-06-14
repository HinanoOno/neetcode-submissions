# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cnt = 0
        def dfs (root):
            nonlocal k
            if not root:
                return 
            ans = root
            tmp = None
            cnt = 0
            while root:
                nex = root.next
                root.next = tmp
                tmp = root
                root = nex
                cnt += 1
                if cnt==k:
                    nex = dfs(root)
                    res = tmp
                    while tmp and tmp.next:
                        tmp = tmp.next
                    tmp.next = nex
                    return res
            if cnt<k:
                cur = None
                while tmp:
                    nex = tmp.next
                    tmp.next = cur
                    cur = tmp
                    tmp = nex
                return cur
            return 
        return dfs(head)




        