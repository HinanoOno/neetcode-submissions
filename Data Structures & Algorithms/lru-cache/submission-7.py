class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.first,self.last = Node(-1,-1),Node(-1,-1)
        self.first.next,self.last.prev = self.last,self.first
        self.cache = {}
    # 0->0
    def remove(self,node):
        pre,nex = node.prev,node.next
        pre.next,nex.prev = nex,pre
        
    def insert(self, node):
        pre,nex = self.last.prev,self.last
        pre.next,node.prev = node,pre
        nex.prev,node.next = node,self.last 
        #0->1->0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.insert(node)
        self.cache[key] = node
        
        if len(self.cache) > self.capacity:
            lru = self.first.next
            self.remove(lru)
            del self.cache[lru.key]

        