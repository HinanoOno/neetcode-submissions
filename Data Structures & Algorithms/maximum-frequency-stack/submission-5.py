class FreqStack:

    def __init__(self):
        self.cnt = Counter()
        self.stack = defaultdict(list)
        self.max_v = 0
        
    def push(self, val: int) -> None:
        self.cnt[val]+=1
        self.stack[self.cnt[val]].append(val)
        if self.cnt[val]>self.max_v:
            self.max_v = self.cnt[val]
        #print(self.stack,self.max_v)
        

    def pop(self) -> int:

        num = self.stack[self.max_v].pop()
        self.cnt[num]-=1
        if not self.stack[self.max_v]:
            self.max_v -= 1
        return num

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()