# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        f,s = ListNode(0,head),ListNode(0,head)
        res = s
        if head.next is None:
            return None
        for i in range(n):
            f = f.next
        print(f.val)
        while f.next is not None:
            f = f.next
            s = s.next
        print(f.val)
        s.next = s.next.next
        return res.next
        

# [1,2,3,4]
# 2
# f= 4 s=""
