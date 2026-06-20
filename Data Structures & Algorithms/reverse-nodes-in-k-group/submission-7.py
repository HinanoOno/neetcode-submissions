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
        def dfs(node):
            tmp = None
            cnt = 0
            head = node
            while head:
                nex = head.next
                head.next = tmp
                tmp = head
                head = nex
                cnt += 1
                #反転後の先頭(prev), 反転後の末尾(node), 次のグループの開始地点(curr)
                if cnt==k:
                    return (tmp,node,head)
            return None,None
        ans = ListNode(0)
        res = ans
        top = head
        for i  in range(time):
            tmp,node,head = dfs(top)
            top = head
            ans.next = tmp
            ans = node
        ans.next = top
        return res.next

            

