# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=None, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        n = len(lists)

        
        def compare(x,ans):
            if not x:
                return None
            res = ListNode()
            prev = ans
            ans = res
            while prev and x:
                if prev.val>x.val:
                    res.next = x
                    x = x.next
                else:
                    res.next = prev
                    prev = prev.next
                res = res.next
            while prev:
                res.next = prev
                prev = prev.next
                res = res.next
            while x:
                res.next = x
                x = x.next
                res = res.next
            print(ans.next.val)
            return ans.next
           
        if not lists or lists[0] == []:
            return None
        ans = lists[0]
        for i in range(1,n):
            cur = compare(lists[i],ans)
            ans = cur
        return ans

            
                
