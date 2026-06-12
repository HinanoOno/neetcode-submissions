class MedianFinder:

    def __init__(self):
        self.small,self.big = [],[]
    
    # s[-1.-2], b[3]
    def addNum(self, num: int) -> None:
        if not self.small or -self.small[0]>num:
            heapq.heappush(self.small,-num)
        else:
            heapq.heappush(self.big,num)
        while len(self.small)<len(self.big):
            num = heapq.heappop(self.big)
            heapq.heappush(self.small,-num)
        while len(self.small)>len(self.big)+1:
            num = heapq.heappop(self.small)
            heapq.heappush(self.big,-num)
        #print(self.big,self.small)

    def findMedian(self) -> float:
        if len(self.small)>len(self.big):
            return -self.small[0]
        elif len(self.small)==len(self.big):
            return (-self.small[0]+self.big[0])/2
        else:
            return -1