import bisect
class MinStack:

    def __init__(self):
        self.stack = []
        self.orders = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.orders or self.orders[-1]<val:
            self.orders.append(val)
        else:
            idx = bisect.bisect_left(self.orders,val)
            self.orders.insert(idx,val)
            print(self.orders)
        
    def pop(self) -> None:
        num = self.stack.pop()
        self.orders.remove(num)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.orders[0]

        
# [1,2,0]
