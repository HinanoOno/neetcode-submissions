# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    
        n = len(lists)
        if not lists:
            return 
        def merge(a,b):
            if not a:
                return b
            if not b:
                return a
            ans = ListNode(0)
            res = ans
            while a and b:
                if a.val<b.val:
                    ans.next = a
                    a = a.next
                else:
                    ans.next =b
                    b = b.next
                ans = ans.next
            if a:
                ans.next = a
            if b:
                ans.next = b
            return res.next
        if len(lists)<=1:
            return [lists[0]]
        ans = lists[0]
        for i in range(1,n):
            ans = merge(ans,lists[i])
        return ans
