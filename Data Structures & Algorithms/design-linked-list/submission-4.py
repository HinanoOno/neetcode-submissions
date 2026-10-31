class Node:  
    def __init__(self,val=0):
        self.val = val
        self.next = None
        self.prev = None
class MyLinkedList:

    def __init__(self):
        self.head,self.tail = Node(0),Node(0)
        self.head.next,self.tail.prev = self.tail,self.head

    def get(self, index: int) -> int:
        tmp = self.head.next
        cnt = 0
        while tmp!=self.tail:
            if cnt==index:
                return tmp.val
            cnt += 1
            tmp = tmp.next
        return -1
        

    def addAtHead(self, val: int) -> None:
        nex = self.head.next
        node = Node(val)
        self.head.next,nex.prev = node,node
        node.next,node.prev = nex,self.head
        

    def addAtTail(self, val: int) -> None:
        prev = self.tail.prev
        node = Node(val)
        self.tail.prev,prev.next = node,node
        node.next,node.prev = self.tail,prev

    def addAtIndex(self, index: int, val: int) -> None:
        tmp = self.head.next
        cnt = 0
        prev = self.head
        while tmp!=self.tail:

            if cnt==index:
                node = Node(val)
                prev.next,tmp.prev = node,node
                node.next,node.prev = tmp,prev
                return 
            prev = tmp
            cnt += 1
            tmp = tmp.next
        if cnt == index:
            self.addAtTail(val)
        return -1
        

    def deleteAtIndex(self, index: int) -> None:
        tmp = self.head.next
        cnt = 0
        prev = self.head
        while tmp!=self.tail:
            nex = tmp.next
            if cnt==index:
                prev.next,nex.prev = nex,prev
                return 
            prev = tmp
            cnt += 1
            tmp = tmp.next
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)