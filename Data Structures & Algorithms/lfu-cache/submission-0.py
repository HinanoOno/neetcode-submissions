class Node:
    def __init__(self,key=0,val=0):
        self.val = val
        self.key = key
        self.freq = 1
        self.prev = None
        self.next = None
class List:
    def __init__(self):
        self.size = 0
        self.head,self.last = Node(),Node()
        self.head.next,self.last.prev = self.last,self.head

class LFUCache:

    def __init__(self, capacity: int):
        self.c = capacity
        self.nodes = {}       # key -> ListNode
        self.freq = {} # freq -> List
        self.min_freq = 0

    def remove(self,node,cnt):
        nodes = self.freq[cnt]
        pre = node.prev
        nex = node.next
        pre.next,nex.prev = nex,pre
        nodes.size-=1
        if nodes.size==0:
            del self.freq[cnt]
    
    def insert(self,node,cnt):
        node.freq = cnt
        if cnt in self.freq:
            nodes = self.freq[cnt]
            nodes.size += 1
            pre,nex = nodes.last.prev,nodes.last
            pre.next,nex.prev = node,node
            node.next,node.prev = nex,pre
        else:
            l = List()
            l.size += 1
            nex = l.head.next
            l.head.next,nex.prev = node,node
            node.next,node.prev = nex,l.head
            self.freq[cnt] = l

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            cnt = node.freq
            self.remove(node,cnt)
            if cnt == self.min_freq and cnt not in self.freq:
                self.min_freq += 1
            self.insert(node,cnt+1)
            return node.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        if self.c == 0:
            return
        if len(self.nodes)==self.c:
            nodes = self.freq[self.min_freq]
            target = nodes.head.next
            del self.nodes[target.key]
            self.remove(target,self.min_freq)
            if self.min_freq not in self.freq:
                self.min_freq += 1
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            cnt = node.freq
            self.remove(node,cnt)
            if cnt == self.min_freq and cnt not in self.freq:
                self.min_freq += 1
            self.insert(node,cnt+1)
            self.nodes[key] = node
        else:
            new_node = Node(key,value)
            self.nodes[key] = new_node
            if 1 in self.freq:
                l = self.freq[1]
                l.size += 1
                last,pre = l.last,l.last.prev
                pre.next,last.prev = new_node,new_node
                new_node.next,new_node.prev = last,pre
            else:
                l = List()
                l.size += 1
                nex = l.head.next
                l.head.next,nex.prev = new_node,new_node
                new_node.next,new_node.prev = nex,l.head
                self.freq[1] = l
            self.min_freq = 1
            
        
            


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)