class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(self.nums)>k:
            heapq.heappop(self.nums)
        print(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums)<self.k:
            heapq.heappush(self.nums,val)
        elif self.nums and self.nums[0]<val:
            num = heapq.heappop(self.nums)
            heapq.heappush(self.nums,val)
        return self.nums[0] if self.nums else -1
        
# [1,2,3,3,3]
# [1,2,3,3,3,5,6,7]
# 
