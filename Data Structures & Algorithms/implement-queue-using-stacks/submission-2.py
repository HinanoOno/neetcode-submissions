class MyQueue:

    def __init__(self):
        self.q = deque([])
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        num = self.q.popleft()
        return num
        

    def peek(self) -> int:
        return self.q[0] 
        

    def empty(self) -> bool:
        return True if not self.q else False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()