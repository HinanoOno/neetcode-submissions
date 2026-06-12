# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ans = head
        f,s = head,head
        while f and f.next:
            f =f.next.next
            s = s.next #6
        prev,cur = None,s.next
        s.next = None
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
    
        f,s = head,prev
        while s:
            nex = f.next
            prev_nex = s.next
            f.next = s #2->8
            s.next = nex
            f = nex
            s = prev_nex
        


# 0<-6<-8