# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        res = ListNode()
        ans = res
        for i in range(len(lists)):
            heapq.heappush(q,(lists[i].val,i))
        while q:
            num,x = heapq.heappop(q)
            res.next = ListNode(num)
            res = res.next
            if lists[x].next:
                lists[x] = lists[x].next
                heapq.heappush(q,(lists[x].val,x))
        return ans.next

# lists = [[1,2,4],[1,3,5],[3,6]]
# q = [1,1,3]
# 1, q= [1,1,3,2]