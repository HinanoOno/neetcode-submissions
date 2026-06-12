# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        res = ans
        plus = 0
        while l1 or l2 or plus:
            p = l1.val if l1 else 0
            q = l2.val if l2 else 0
            cur = p+q+plus

            plus = 0
            if cur>=10:
                plus = cur//10
                cur = cur%10
            ans.next = ListNode(cur)
            ans = ans.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return res.next

        