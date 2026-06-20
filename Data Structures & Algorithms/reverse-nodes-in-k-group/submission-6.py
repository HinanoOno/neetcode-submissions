# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        cnt = 0
        while cur:
            cur = cur.next
            cnt += 1
        time = cnt//k
        def dfs(head):
            tmp = None
            cnt = 0
            while head:
                nex = head.next
                head.next = tmp
                tmp = head
                head = nex
                cnt += 1
                if cnt==k:
                    return (tmp,head)
            return None,None
        top = head
        ans = ListNode(0)
        res = ans
        for i  in range(time):
            tmp,head = dfs(top)
            ans.next= tmp
            while tmp.next:
                tmp = tmp.next
            top = head
            ans = tmp
        if top:
            ans.next = top
        return res.next

