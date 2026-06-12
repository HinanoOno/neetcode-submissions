"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 
        tmp = head
        cur = head
        dp ={}
        while tmp:
            dp[tmp]= Node(tmp.val)
            tmp = tmp.next
        print(dp)

        while cur:
            dp[cur].next = dp.get(cur.next)
            dp[cur].random = dp.get(cur.random)
            cur = cur.next
        return dp[head]
        